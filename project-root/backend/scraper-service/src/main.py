from sites import hepsiemlak_scraper, emlakjet_scraper

def main():
    # Run both scraper modules sequentially for demonstration.
    # You may later run them concurrently or schedule them as needed.
    hepsiemlak_scraper.scrape_site()
    emlakjet_scraper.scrape_site()

if __name__ == "__main__":
    main()
