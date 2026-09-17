import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

webpage = webdriver.Chrome()
webpage.get("https://automationexercise.com/")


all_links = webpage.find_elements(By.TAG_NAME, value='a')

for link in all_links:
    # it gets the real form of URL ex :https://the-internet.herokuapp.com/status_codes/404
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code <= 400:
        print(f"The Link {href} : {response.status_code}")

webpage.quit()