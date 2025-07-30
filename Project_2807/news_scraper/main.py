from core.scraper import scrape, headline_generator
# from utils.decorators import log_time  # Optional usage

def main():
    url = "https://www.bbc.com/news"  # You can replace with any news site
    print(f"Scraping headlines from: {url}")

    headlines = scrape(url)

    if not headlines:
        print("No headlines found or an error occurred.")
        return

    print("\n--- Headlines ---")
    for headline in headline_generator(headlines):
        print(f"• {headline}")

if __name__ == "__main__":
    main()
