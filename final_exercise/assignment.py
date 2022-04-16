from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def webDriver(url):
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    
    driver.get(url)

    # Wait until the cookie element is visible and utomatically close it
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))).click()

    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "popupCloseIcon largeBannerCloser"))).click()
    time.sleep(2)
    # Wait until the button to filter the date is visible
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "widgetField")))

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

    # Wait until the filter is applied
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "curr_table")))


    # Step 2: Parse HTML code and grab tables with Beautiful Soup
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # tables = soup.find_all('table')
    tables = soup.find('table', { 'class' : 'genTbl closedTbl historicalTbl' })

    # Step 3: Read tables with Pandas read_html()
    df = pd.read_html(str(tables))[0]

    print(f'Total tables: {len(df)}')
    df=df.drop(columns=['High', 'Low','Open'])
    # print(df)
    driver.close()
    return df

    


if __name__ == '__main__':

    # Global stocks
    df_amundi = webDriver("https://www.investing.com/funds/amundi-msci-wrld-ae-c-historical-data")

    # Save the dataset in a csv
    df_amundi.to_csv("amundi-msci-wrld-ae-c.csv")
    df_amundi.to_csv(index=True)

    # Corporate bonds
    df_ishares = webDriver("https://www.investing.com/etfs/ishares-global-corporate-bond-$-historical-data")

    # Save the dataset in a csv
    df_ishares.to_csv("ishares-global-corporate-bond-$.csv")
    df_ishares.to_csv(index=True)

    # Public or government bonds
    df_trackers = webDriver("https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5-historical-data")

    # Save the dataset in a csv
    df_trackers.to_csv("db-x-trackers-ii-global-sovereign-5.csv")
    df_trackers.to_csv(index=True)

    # Gold
    df_gold = webDriver("https://www.investing.com/etfs/spdr-gold-trust-historical-data")

    # Save the dataset in a csv
    df_gold.to_csv("spdr-gold-trust.csv")
    df_gold.to_csv(index=True)

    # Cash
    df_usdollar = webDriver("https://www.investing.com/indices/usdollar-historical-data")

    # Save the dataset in a csv
    df_usdollar.to_csv("usdollar.csv")
    df_usdollar.to_csv(index=True)