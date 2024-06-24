import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://indiahikes.com/nafran-valley-trek"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the h1 tags in the HTML
h1_tags = soup.find_all("h1")

# Extract the contents of the h1 tags
h1_contents = [tag.text for tag in h1_tags]

# Print the extracted contents
for content in h1_contents:
    print(content)