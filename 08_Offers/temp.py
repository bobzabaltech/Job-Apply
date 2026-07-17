import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.rheinmetall.com/en/career/vacancies?page={}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

jobs = {}
page = 1

while True:
    url = BASE_URL.format(page)

    print(f"Processing page {page}...")

    response = requests.get(url, headers=headers, timeout=30)

    if response.status_code != 200:
        print(f"Stopping at page {page} (HTTP {response.status_code})")
        break

    soup = BeautifulSoup(response.text, "html.parser")

    links_found = 0

    for a in soup.find_all("a", href=True):

        href = a["href"]
        title = a.get_text(strip=True)

        if not title:
            continue

        if "/job/" not in href:
            continue

        full_url = urljoin("https://www.rheinmetall.com", href)

        jobs[full_url] = title
        links_found += 1

    if links_found == 0:
        print(f"No jobs found on page {page}. Stopping.")
        break

    page += 1

print(f"\nTotal unique jobs found: {len(jobs)}")

with open(
    "rheinmetall_jobs.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "job_title",
        "job_url"
    ])

    for url, title in jobs.items():
        writer.writerow([
            title,
            url
        ])

print("CSV saved as rheinmetall_jobs.csv")