import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extracting the titles of all the links on the page
        link_titles = [link.get('title') for link in soup.find_all('a', {'title': True})]

        # Print the extracted titles
        print("Titles of links on the page:")
        for title in link_titles:
            print("- " + title)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Specify the URL of the webpage you want to scrape
    url_to_scrape = "https://github.com/heartofstoneclothing"

    # Call the web scraper function
    simple_web_scraper(url_to_scrape)
