import requests
import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://www.mizuhobank.co.jp/rate_fee/rate_interest.html"
session = HTMLSession()
r = session.get(url)

r.html.render()

tbody_tag = r.html.find("tbody", first=True)
print(tbody_tag.text)

