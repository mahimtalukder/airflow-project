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
time.sleep(10)

phones = browser.find_elements("css selector",'div.text-base-regular')

for element in phones:
    model = element.find_element("css selector",'span')
    print(model.text)


# with open('file.html', 'w') as file:
#     file.write(browser.page_source)
# print(browser.page_source)



#Wait for 10 seconds
