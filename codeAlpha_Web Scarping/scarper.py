import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target website
url = "https://books.toscrape.com/"

# Send request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book containers
books = soup.find_all('article', class_='product_pod')

# Extract book titles
titles = [book.h3.a['title'] for book in books]

# Convert to DataFrame
df = pd.DataFrame(titles, columns=["Book Title"])

# Save to CSV
df.to_csv('books.csv', index=False)

print("✅ Scraping done! 'books.csv' created successfully.")
