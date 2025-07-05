import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.example.com"

try:
    # Get the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the title tag text
    title = soup.title.string if soup.title else 'No title found'

    # Save title to a file
    with open("page_title.txt", "w") as file:
        file.write(title)

    print(f" Page title extracted and saved: {title}")

except requests.exceptions.RequestException as e:
    print(f" Error fetching the webpage: {e}")