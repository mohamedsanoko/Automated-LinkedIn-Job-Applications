from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/feed/")

time.sleep(5)


# driver.implicitly_wait(10)
# sign_in_button = driver.find_element(By.CSS_SELECTOR, value="div a")
# sign_in_button.click()
