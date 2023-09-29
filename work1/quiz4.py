import requests
import re
from bs4 import BeautifulSoup

# 4

print(4)
web_site_html_text = requests.get("https://qiita.com/advent-calendar/2016/crawler").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

a_tag = soup.find_all("a", class_="style-3ki7ar")

# 一行ver
# result = [i.get('href') for i in soup.find_all("a", class_="style-3ki7ar")]
# print(result)


for i in a_tag:
    print(i.get('href'))

