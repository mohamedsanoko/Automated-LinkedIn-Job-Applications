from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

EMAIL = os.environ.get("EMAIL", "Key does not exist")
PASSWORD = os.environ.get("PASSWORD", "Key does not exist")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/feed/")

time.sleep(3)

sign_in_link = driver.find_element(By.CLASS_NAME, value="main__sign-in-link")
sign_in_link.click()
# driver.implicitly_wait(10)
# sign_in_button = driver.find_element(By.CSS_SELECTOR, value="div a")
# sign_in_button.click()
