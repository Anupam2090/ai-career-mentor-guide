# market_scraper.py

import requests
from bs4 import BeautifulSoup

def get_job_trends(keyword):
    """
    Scrapes Indeed.com for job postings related to the given keyword.
    Returns the count of job listings found and job search links (clickable).
    """
    try:
        url_indeed = f"https://www.indeed.com/jobs?q={keyword.replace(' ', '+')}&l="
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        res = requests.get(url_indeed, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        jobs = soup.find_all("div", class_="job_seen_beacon")
        job_count = len(jobs)

        # LinkedIn job search link (not scraping)
        url_linkedin = f"https://www.linkedin.com/jobs/search/?keywords={keyword.replace(' ', '%20')}"

        return (
            # f"<p>🔍 <b>{job_count}</b> jobs found for <b>{keyword}</b> on Indeed.</p>"
            # f"<p>🚀 In this field, some of the most in-demand roles are: <br><br>🔗 <a href='{url_indeed}' target='_blank'>View on Indeed</a></p>"
            # f"<p>🔗 <a href='{url_linkedin}' target='_blank'>View on LinkedIn</a></p>"
        )

    except Exception as e:
        return f"<p style='color:red;'>⚠️ Error fetching job trends: {str(e)}</p>"

def get_market_trends(career_goal):
    """
    Combines static trend text with live job data scraped from Indeed
    and adds LinkedIn job search URL (all in clickable HTML format).
    """
    static_trend = (
        f"<p>📊 Based on current trends, the demand for <b>{career_goal}</b> is rising.</p>"
        # f"<p>🚀 In this field, some of the most in-demand roles are:</p>"
        f"<p>🌐 Suggested platforms: LinkedIn, Indeed.</p>"
    )
    job_data = get_job_trends(career_goal)
    return static_trend + job_data
