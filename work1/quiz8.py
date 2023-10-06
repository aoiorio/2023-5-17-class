from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome()

driver.get('https://www.google.com/')
time.sleep(1)

#pythonを検索
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys('python')
search_box.submit()

print("beautiful soup ver")
# for h3 in driver.find_elements(By.XPATH, '//*[@id="rso"]'):
#     print(h3.text)

page_html = driver.page_source

# 検索結果のリンクを取得
pageSoup = BeautifulSoup(page_html, 'html.parser')



h3 = pageSoup.find_all(class_="LC20lb MBeuO DKV0Md")

for i in h3:
    print(i.text)

# something_went_wrong = driver.find_elements(by=By.CLASS_NAME, value="LC20lb MBeuO DKV0Md")

print("---------------------find_elements ver-----------------------------")

# time.sleepを挟まないと、submitした後にすぐ取得してしまってエラーが出る
time.sleep(2)

elements = driver.find_elements(by=By.CLASS_NAME, value="MjjYud")

for elem in elements:
    try:
        h3_tag = elem.find_element(By.TAG_NAME, "h3")
        print(h3_tag.text)
    except Exception:
        print("Please ignore the error")

driver.quit()