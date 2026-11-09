# Task 3: Web Scraper for News Headlines
# Python Developer Internship

import requests
from bs4 import BeautifulSoup

# Public news website
url = "https://www.bbc.com/news"

# Browser-like User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}


def scrape_headlines():
    try:
        print("Fetching news headlines...")

        # Send GET request
        response = requests.get(url, headers=headers, timeout=15)

        # Check HTTP response
        response.raise_for_status()

        # Parse webpage HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find headline headings
        heading_tags = soup.find_all(["h2", "h3"])

        headlines = []
        for heading in heading_tags:
            headline = heading.get_text(" ", strip=True)

            if headline and headline not in headlines:
                headlines.append(headline)

        if not headlines:
            print("No headlines found. The website structure may have changed.")
            return

        # Save headlines to a text file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            file.write("TOP NEWS HEADLINES\n")
            file.write("=" * 40 + "\n\n")

            for number, headline in enumerate(headlines[:30], start=1):
                file.write(f"{number}. {headline}\n")

        print(f"Successfully saved {min(len(headlines), 30)} headlines!")
        print("Check the headlines.txt file.")

    except requests.exceptions.RequestException as error:
        print("Error fetching the website:", error)

    except Exception as error:
        print("An unexpected error occurred:", error)


if __name__ == "__main__":
    scrape_headlines()