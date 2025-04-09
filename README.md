# 🎓 Personalized AI Career Mentor

An intelligent web application built with Flask and Google's Gemini API that analyzes user resumes, generates personalized career roadmaps, and forecasts market trends.

---

## 🚀 Features

---

- ✅ **Resume Analysis** using Gemini AI  
- 🎯 **Career Roadmap Generation** based on user goals  
- 🔗 **Clickable job links for Indeed and LinkedIn** for informed decisions  
- 📄 Upload your PDF resume and get insights instantly  

---

## 🧠 How It Works

---

1. Upload your **resume (PDF format)**.
2. Enter your **career goal** (e.g., Data Scientist, Cloud Engineer etc).
3. The app:
   - Analyzes your resume using Gemini API.
   - Generates personalized roadmap steps.
   - link provide corresponding Your Career Goal
4. All insights are presented in a simple web interface.

---

## 📁 Project Structure with File Descriptions

---

ai-career-mentor-guide/ │ ├── app.py

Main Flask app: handles routes, file uploads, and rendering responses.
│ ├── gemini_analyzer.py

Uses Gemini API to analyze resume text and provide smart suggestions.
│ ├── resume_parser.py

Extracts raw text from uploaded PDF resumes using PyMuPDF or similar.
│ ├── career_roadmap.py

Generates a personalized roadmap for a given career goal.
│ ├── market_scraper.py

Scrapes the web for live career trends and in-demand skills/tools.
│ ├── credentials.ini

Holds the Gemini API key securely. (DO NOT share publicly)
│ ├── uploads/

Stores uploaded resumes temporarily for processing.
│ └── templates/ └── index.html # Main web interface: form for uploading resume and displaying results.

---

# ⚙️ Setup Instructions

---

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-career-mentor-guide.git
cd ai-career-mentor-guide

```

# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

```

# Store the API Key
Create a credentials.ini file in your project root:
[google]
api_key=your-api-key-here

```

# Run the Application

---
python app.py

```
```
# 🖥️ Output Example

---

When you run the app and upload your resume:

## ✅ Resume Analysis (Gemini)
- Skills: Python, SQL, Machine Learning
- Gaps: No certifications in Cloud or Data Engineering
- Suggested Courses: Google Data Analytics, AWS Certified Solutions Architect

## 🗺️ Career Roadmap (AI-Powered)
1. Master SQL and Python fundamentals
2. Learn data visualization (Tableau, Power BI)
3. Earn Google Data Analytics certification
4. Gain experience through Kaggle projects
5. Apply to entry-level data roles

## 📈 Market Trends (Live)
📊 Based on current trends, the demand for **Data Scientist** is rising.  
🚀 Relevant roles include Machine Learning Engineer, Data Analyst, and AI Researcher.  
🌐 Suggested platforms: LinkedIn, Indeed, HackerRank.

🔍 3,215 jobs found for 'Data Scientist' on Indeed  
🔗 [View on Indeed](https://www.indeed.com/jobs?q=Data+Scientist&l=)  
🔗 [View on LinkedIn](https://www.linkedin.com/jobs/search/?keywords=Data%20Scientist)

```
```

## 🌐 GitHub Integration

```

The project includes detailed steps for version control and pushing code to GitHub for easy collaboration and tracking.

```



