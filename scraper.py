import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_job_listings(query):
   
    URL = f"https://www.linkedin.com/jobs/search/?keywords={query.replace(' ', '%20')}"
    
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_card in soup.find_all("div", class_="base-card"):
        title = job_card.find("h3", class_="base-search-card__title").text.strip()
        company = job_card.find("h4", class_="base-search-card__subtitle").text.strip()
        location = job_card.find("span", class_="job-search-card__location").text.strip()
        link = job_card.find("a", class_="base-card__full-link")["href"]
        
        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Link": link
        })

    return jobs
