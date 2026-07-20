import csv
import json
import time
import requests

from bs4 import BeautifulSoup


INPUT_CSV = "base.csv"
OUTPUT_JSON = "jobs.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}


def extract_job_description(html):

    soup = BeautifulSoup(html, "html.parser")

    selectors = [
        ".job-description",
        ".vacancy-detail",
        ".job-content",
        ".content",
        "article",
        "main"
    ]

    for selector in selectors:

        section = soup.select_one(selector)

        if section:

            text = section.get_text(
                separator="\n",
                strip=True
            )

            if len(text) > 1000:
                return text

    body = soup.get_text(
        separator="\n",
        strip=True
    )

    return body


def main():

    results = []

    with open(
        INPUT_CSV,
        newline="",
        encoding="utf-8"
    ) as f:

        reader = csv.DictReader(f)

        for row in reader:

            title = row["job_title"].strip()
            url = row["job_url"].strip()

            print(f"Processing: {title}")

            try:

                response = requests.get(
                    url,
                    headers=HEADERS,
                    timeout=30
                )

                response.raise_for_status()

                description = extract_job_description(
                    response.text
                )

                results.append(
                    {
                        "job_title": title,
                        "job_url": url,
                        "job_description": description
                    }
                )

                time.sleep(1)

            except Exception as e:

                print(f"ERROR: {url}")
                print(e)

                results.append(
                    {
                        "job_title": title,
                        "job_url": url,
                        "job_description": None
                    }
                )

    with open(
        OUTPUT_JSON,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"\nSaved {len(results)} jobs to {OUTPUT_JSON}"
    )


if __name__ == "__main__":
    main()