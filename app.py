import os
import fitz  # PyMuPDF
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"

# Initialize Flask app
app = Flask(__name__)
CORS(app)

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def analyze_resume(text, job_description=""):
    system_prompt = (
        "You are a resume analysis assistant. Analyze the resume text provided, "
        "and return structured JSON with sections like skills, experience, education, and a score. "
        "If a job description is provided, evaluate match relevance."
    )

    user_prompt = f"Resume Text:\n{text[:3000]}\n\n"
    if job_description:
        user_prompt += f"\nJob Description:\n{job_description[:1000]}"

    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"},
    )

    return response.choices[0].message.content

@app.route('/analyze_resume', methods=['POST'])
def analyze_resume_endpoint():
    try:
        if 'resume' not in request.files:
            return jsonify({"error": "No resume file uploaded"}), 400
        resume_file = request.files['resume']
        job_description = request.form.get('job_description', '')

        # Save temporarily
        file_path = os.path.join("tmp", resume_file.filename)
        os.makedirs("tmp", exist_ok=True)
        resume_file.save(file_path)

        # Extract and analyze
        resume_text = extract_text_from_pdf(file_path)
        analysis = analyze_resume(resume_text, job_description)

        return jsonify({"success": True, "analysis": analysis})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)