from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
url = "https://indiahikes.com/chandrakhani-pass-trek#quick-itinerary"

driver.get(url)
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

#title
title = soup.find("h1", class_="BannerWIthCaption_bannerCaption__5ZPkg").text

#difficulty and duration
details = soup.find_all("div", class_="QuickInfoWidget_content-box__HdwqQ")
for detail in details:
    if(detail.h3.text == "TREK DIFFICULTY"):
        difficulty = detail.p.text
    elif(detail.h3.text == "TREK DURATION"):
        duration = detail.p.text

#photos
photos = soup.find("div", class_="highlightedSnippet_highlightedSnippet__XAvlw").p.a['href']

#fees
fees_div = soup.find("div", class_="FeeDetails_feeOptions__XVibQ")
contents = fees_div
fees = contents.find("div", class_="mx-2").p.text
trek_data = {
    "url": url,
    "title": title,
    "fees": fees,
    "difficulty": difficulty,
    "duration": duration,
    "photos": photos,
}

print(trek_data)

driver.quit()