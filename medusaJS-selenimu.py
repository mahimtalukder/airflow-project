## Run selenium and chrome driver to scrape data from cloudbytes.dev

import time

import os.path

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options



## Setup chrome options

chrome_options = Options()

chrome_options.add_argument("--headless") # Ensure GUI is off

chrome_options.add_argument("--no-sandbox")



# Set path to chromedriver as per your configuration

homedir = os.path.expanduser("~")

webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")



# Choose Chrome Browser

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)



# Get page

browser.get("http://localhost:8000/store")



# Extract description from page and print

products = browser.find_elements("css selector",'div.text-base-regular')

print("Product Name ------------------------------- Product Price")
for element in products:

    title = element.find_element("css selector",'span')
    price = element.find_element("css selector",'span.font-semibold')
    
    print(title.text + " ------------------------------- " + price.text)



#Wait for 10 seconds

time.sleep(10)