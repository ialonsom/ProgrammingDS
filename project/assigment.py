from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://www.investing.com/etfs/ishares-global-corporate-bond-$-historical-data")
time.sleep (1)


# Click and open the Date Picker
driver.find_element_by_id("widgetField").click()

# driver.find_element_by_xpath('//*[@id="widgetField"]'.format(end_date_calendar)).click()

# driver.find_element_by_xpath(
#         "//button[@aria-label='{}']".format(end_date_calendar)).click()


# In the URL there are 2 ’input ’ elements of type =" search "
# A different aspect must be found -> @placeholder attribute
elemList = driver.find_element_by_id("startDate")
print("elemList", elemList)
# Make sure just one element is found
# assert (len(elemList) == 1)
# inputElement = elemList[0]
# Clear the input text field , in case there is some default value
# elemList.clear()
# Write in the text field the search term
# inputElement.send_keys("01/01/2020")
# - 12/31/2020


# Step 2: Parse HTML code and grab tables with Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

# tables = soup.find_all('table')
tables = soup.find('table', { 'class' : 'genTbl closedTbl historicalTbl' })

# Step 3: Read tables with Pandas read_html()
dfs = pd.read_html(str(tables))

print(f'Total tables: {len(dfs)}')
print(dfs)

driver.close()
