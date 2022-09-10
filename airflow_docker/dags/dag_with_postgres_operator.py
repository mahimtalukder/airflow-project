from datetime import datetime, timedelta
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'clickSpikes',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet():
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")

    # Set path to chromedriver as per your configuration
    homedir = os.path.expanduser("~")
    webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

    # Choose Chrome Browser
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Get page
    browser.get("https://www.daraz.com.bd/catalog/?_keyori=ss&from=input&q=xioami&spm=a2a0e.searchlist.search.go.5cce6567NTTDQQ&style=list")


    # Extract description from page and print
    phones = browser.find_elements("css selector",'div.title--vuYqg')
    for element in phones:
        model = element.find_element("css selector",'a')
        print(model.text)


    #Wait for 10 seconds
    time.sleep(10)
    browser.quit()
     

with DAG(
    dag_id = "python_operator_v2",
    default_args = default_args,
    description = "Tesing the python operator",
    start_date = datetime(2022, 9, 9, 11),
    schedule_interval = "@daily"
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task1
