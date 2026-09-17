from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/login")

username = 'EducationOnly710@gmail.com'
password = 'anything'

username_input = driver.find_element(By.CSS_SELECTOR, value="input[data-qa='login-email']")
password_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")

result = driver.find_element(By.XPATH,"//header[@id='header']//li[1]//a[1]" )
print(result.is_displayed())

username_input.send_keys(username)
password_input.send_keys(password)
time.sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")
login_button.click()



driver.quit()

#assert result.text == 'Products'
