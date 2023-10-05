import requests
import re
from bs4 import BeautifulSoup
# from requests_html import HTMLSession
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# session = HTMLSession()
# r = session.get(url)

# r.html.render()

# tbody_tag = r.html.find("tbody", first=True)
# print(tbody_tag.text)

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


driver.get("https://www.mizuhobank.co.jp/rate_fee/rate_interest.html")
url = "https://www.mizuhobank.co.jp/rate_fee/rate_interest.html"

sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print(soup.find("tbody").text)

