# 📄 Resume Analyzer API

**AI-powered Resume Analysis API using Flask and OpenAI GPT-4o-mini. Upload a PDF resume and get structured insights, skill extraction, and optional job match scoring.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-lightgrey)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Features

- 🔍 Extracts structured data (skills, experience, education) from resumes
- 📄 Accepts PDF file uploads
- 🤖 Analyzes content using OpenAI's GPT-4o-mini
- 🧠 Supports job description input for relevance scoring
- 🌐 CORS-enabled, easy integration with frontends

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Flask**
- **OpenAI GPT-4o-mini**
- **PyMuPDF (fitz)**
- **Flask-CORS**
- **dotenv**

---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/resume-analyzer-api.git
cd resume-analyzer-api

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenAI API Key to a .env file
echo "OPENAI_API_KEY=your_openai_key" > .env
