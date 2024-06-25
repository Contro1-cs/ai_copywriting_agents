from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the Selenium webdriver
driver = webdriver.Chrome()

# URL of the website
url = "https://indiahikes.com/chandrakhani-pass-trek#quick-itinerary"

driver.get(url)

# Get the page source after the JavaScript has executed
page_source = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find the div with class "card TrekInfoOverview_feeCard___Ruu6"
div = soup.find("div", class_="FeeDetails_feeOptions__XVibQ")

# Extract the contents of the div
contents = div
fees = contents.find("div", class_="mx-2").p.text

# Close the Selenium webdriver
driver.quit()