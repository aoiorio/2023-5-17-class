from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome()

driver.get('https://www.google.com/')
time.sleep(2)
#pythonを検索
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys('python')
search_box.submit()
time.sleep(2)

driver.quit()
