from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3835957961&f_AL=true&geoId=101174742&keywords=data%20scientist&location=Canada&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true")


