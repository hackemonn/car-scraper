# Car Scraper Project

A Python project to **collect and structure used car listings** focusing on Ford Focus cars in Budapest.  

The project demonstrates **web scraping with Selenium** for JavaScript-rendered pages, **HTML parsing with BeautifulSoup**, and **data cleaning/export to CSV** containing 520 data.  

---

## Project Goal

- Automate the collection of used car listings from a website that relies on JavaScript.  
- Extract structured data such as **price, year, mileage, fuel type, transmission, engine capacity, color, doors, and location**.  
- Produce a **CSV dataset** suitable for analysis or research.  

---

## Data Origins

- Source website: [kocsi.hu](https://kocsi.hu)  
- Collected data includes:
  - Listing URL  
  - Price (`Jármű ára`)  
  - Year (`Gyártási év`)  
  - Mileage (`Kilométeróra állása`)  
  - Fuel type (`Üzemanyag`)  
  - Transmission (`Váltó`)  
  - Engine capacity (`Hengerűrtartalom`)  
  - Power (`Teljesítmény`)  
  - Color (`Jármű színe`)  
  - Number of doors (`Ajtók száma`)  
  - Seller location (`Location`)  

> **Note:** All data is publicly available on the website. This project is **for educational and research purposes only**.  
- Do **not** use this scraper for commercial purposes.  
- Respect the source website’s [Terms of Service](https://en.wikipedia.org/wiki/Terms_of_service) and any applicable laws.  
- The author is **not responsible** for misuse of the code or data.  


---

## Prerequisites / Steps to Reproduce

### Prerequisites

- **Python 3.9+**
- **Chromium based browser or Firefox** installed
- **ChromeDriver / GeckoDriver** compatible with your browser version
- **Internet connection**

### Steps to Reproduce



```bash
1. **Clone the repository:**

git clone https://github.com/<your-username>/car_scraper_project.git
cd car_scraper_project

2. **Install dependencies:**

pip install -r requirements.txt


3. **Ensure ChromeDriver / BraveDriver path is correct in config.py or the script.**

4. **Collect listing URLs:**

cd src
python collect_links.py


5. **Scrape car data:**

cd src
python scrape_data.py


Reads data/links.csv, scrapes each listing, and saves to data/cars_dataset.csv.

6. **View results:**

Open data/cars_dataset.csv in a UTF-8 compatible editor (e.g., VSCode, LibreOffice, Notepad++) to see the structured dataset.

