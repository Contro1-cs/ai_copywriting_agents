from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://indiahikes.com/chandrakhani-pass-trek#quick-itinerary"
driver.get(url)
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")



how_to_reach = soup.find_all("div", class_="d-flex align-items-start flex-wrap mt-1")
content = how_to_reach[0].find("div", class_="p-text-small text-dark mb-2").p

location = content.find("a").text
google_maps_link = content.find("a")["href"]

print("Location:", location)
print("Google Maps Link:", google_maps_link)

driver.quit()