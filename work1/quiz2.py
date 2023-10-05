import requests
import re
from bs4 import BeautifulSoup

# 2
print(2)
web_site_html_text = requests.get("https://www.python.org").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

section_tag = soup.find("div")

events = section_tag.find_all(class_=re.compile("medium-widget event-widget last"))

for event in events:
    print(event.text)
events = soup.select("ul.menu")


top = soup.find('div', class_="event-widget")
ul = top.find('ul')

for li in ul.find_all('li'):
    print(li.time.text, li.a.text)
