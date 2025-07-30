import requests
from bs4 import BeautifulSoup

def scrape(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = {}
        count = 1

        for h in soup.find_all(['h1', 'h2', 'h3']):
            text = h.get_text(strip=True)
            if text and len(text) > 15:  # Filter short titles
                headlines[f"headline_{count}"] = text
                count += 1

        return headlines

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return {}

def headline_generator(headline_dict):
    for key, headline in headline_dict.items():
        yield headline
