import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

webpage = webdriver.Chrome()
webpage.maximize_window()
webpage.get("https://automationexercise.com/")

all_images = webpage.find_elements(By.TAG_NAME, value= 'img')
broken_images = []

for image in all_images:
    img = image.get_attribute('src')
    response = requests.get(img)
    if response.status_code <= 404:
        print(f"This image is verified {img}")



webpage.quit()# It is important to quit the instance
