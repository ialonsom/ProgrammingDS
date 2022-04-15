from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.investing.com/etfs/ishares-global-corporate-bond-$-historical-data")
time.sleep (5)

# A different aspect must be found -> @placeholder attribute
driver.find_element_by_id("widgetField").click()
inputElement = driver.find_element_by_xpath('//*[@id="picker"]')
start_date = driver.find_element_by_id("startDate")
end_date = driver.find_element_by_id("endDate")

start_date.clear()
end_date.clear()
# Write in the text field the search term
start_date.send_keys("01/01/2020")
end_date.send_keys("12/31/2020")

driver.find_element_by_id("applyBtn").click()

time.sleep(5)

# Step 2: Parse HTML code and grab tables with Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

# tables = soup.find_all('table')
tables = soup.find('table', { 'class' : 'genTbl closedTbl historicalTbl' })

# Step 3: Read tables with Pandas read_html()
df = pd.read_html(str(tables))[0]

#print(f'Total tables: {len(df)}')
print(df)

driver.close()
