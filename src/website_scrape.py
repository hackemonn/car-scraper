import time
import csv
import unicodedata
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def clean_text(szoveg):
    return unicodedata.normalize('NFC', szoveg.strip()).replace("\xa0", " ")

field_map = {
    "Jármű ára:": "Price",
    "Gyártási év:": "Year",
    "Kilométeróra állása:": "Mileage",
    "Üzemanyag:": "Fuel",
    "Váltó:": "Transmission",
    "Hengerűrtartalom:": "EngineCapacity",
    "Teljesítmény:": "Power",
    "Jármű színe:": "Color",
    "Ajtók száma:": "Doors"
}

chromedriver_path = r"C:/Users/user/Documents/Codes/chromedriver-win64/chromedriver-win64/chromedriver.exe"
#replace it with your own version

options = Options()
options.binary_location = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
#replace it with your own version

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)


osszes_auto = []

base_url = "https://kocsi.hu"

for i in range(1, 53):
    url = f"https://kocsi.hu/hasznaltauto/budapest/ford/focus/page{i}/"
    driver.get(url)

    time.sleep(3)

    adat = driver.page_source
    soup = BeautifulSoup(adat, "html.parser", from_encoding="utf-8")
    auto_linkek = soup.find_all("a", class_="caption")

    for auto in auto_linkek:
        link = auto.get("href")
        
        if link:
            osszes_auto.append(base_url + link)
    print(f"Lap {i}: {len(auto_linkek)} link összegyűjtve")

print(f"Total links collected: {len(osszes_auto)/2}")

osszes_auto_szurt = []

for i in range(0, len(osszes_auto), 2):
    osszes_auto_szurt.append(osszes_auto[i])

#for i in range(0, len(osszes_auto_szurt)):
    #print(osszes_auto_szurt[i] + "\n")

#print("\nAll links saved to car_links.csv")
print("\nCar data collection successful\n")

columns = ["link"] + list(field_map.values()) + ["Location"]

with open("cars_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

    for id, link in enumerate(osszes_auto_szurt, start=1):
        print(f"Processing {id}/{len(osszes_auto_szurt)}\n")
        driver.get(link)
        time.sleep(2)  # wait for JS to render

        soup = BeautifulSoup(driver.page_source, "html.parser", from_encoding = "utf-8")

        # Initialize car data
        car_data = {v: "" for v in field_map.values()}
        car_data["link"] = link

        # Scrape table data
        tables = soup.find_all("table")
        for table in tables:
            for tr in table.find_all("tr"):
                tds = tr.find_all("td")
                if len(tds) == 2:
                    label = clean_text(tds[0].text)
                    value = clean_text(tds[1].text)
                    if label in field_map:
                        car_data[field_map[label]] = value

        # Scrape location
        try:
            location_element = soup.find(class_="cim")
            car_data["Location"] = clean_text(location_element.text.strip())
        except:
            car_data["Location"] = "Na"
        #Na = Not available 
        
        # Write row to CSV
        writer.writerow(car_data)



print("Dataset complete: cars_dataset.csv")
