from flask import Flask, render_template, request
import os
from resume_parser import extract_text_from_pdf
from gemini_analyzer import analyze_resume
from career_roadmap import generate_roadmap
from market_scraper import get_market_trends

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['resume']
        career_goal = request.form['career_goal']

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            resume_text = extract_text_from_pdf(filepath)
            analysis = analyze_resume(resume_text)
            roadmap = generate_roadmap(career_goal)
            market_trends = get_market_trends(career_goal)

            return render_template("index.html", analysis=analysis, roadmap=roadmap, market_trends=market_trends)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
