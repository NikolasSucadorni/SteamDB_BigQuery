from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://steamdb.info/sales/")

try:
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-sales"))
    )
    
    soup = BeautifulSoup(driver.page_source, "html.parser")

finally:
    driver.quit()


sales_table = soup.find("table", {"class": "table-sales"})

data = []

for row in sales_table.find_all("tr"):
    cells = row.find_all("td")
    if len(cells) > 0:
        game_name = cells[2].get_text(strip=True)
        discount = cells[3].get_text(strip=True)
        price = cells[4].get_text(strip=True)
        rating = cells[5].get_text(strip=True)
        release = cells[6].get_text(strip=True)
        ends = cells[7].get_text(strip=True)
        started = cells[8].get_text(strip=True)
        data.append([game_name, discount, price, rating, release, ends, started])


df = pd.DataFrame(data, columns=["Game", "Discount", "Price", "Rating", "Release", "Ends", "Started"])
df.to_csv("data_steam_sales.csv", index=False)