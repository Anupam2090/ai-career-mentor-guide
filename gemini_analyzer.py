import google.generativeai as genai
from configparser import ConfigParser

# Read API key from credentials.ini
config = ConfigParser()
config.read('credentials.ini')
api_key = config['gemini_ai']['API_KEY']

# Correct way to configure the API
genai.configure(api_key=api_key)

# Use correct model name and method
model = genai.GenerativeModel("gemini-1.5-pro-latest")
  # this is the latest stable version

def analyze_resume(resume_text):
    prompt = f"""
    Analyze the following resume text and provide:
    - Top career paths
    - Relevant certifications
    - A short note if the user should consider changing jobs

    Resume:
    {resume_text}
    """

    # Gemini now uses this method with a list of strings as prompt
    response = model.generate_content([prompt])
    return response.text
