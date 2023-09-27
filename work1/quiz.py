# 1
import requests
import re
from bs4 import BeautifulSoup

# https://intl.cmf.tech/pages/watch-pro
web_site_html_text = requests.get("https://www.python.org").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

jobs = set()
for job in soup.body.ul("li"):
    jobs.add(f"{job.a.string})")

    print(job.a.string)

print("--------------------------------------------------------------------")
# 2
web_site_html_text = requests.get("https://www.python.org").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

section_tag = soup.find("div")

events = section_tag.find_all(class_=re.compile("medium-widget event-widget last"))

for event in events:
    print(event.text)
events = soup.select("ul.menu")

print("---------------------------------------------------------------------")
# 3
web_site_html_text = requests.get("https://www.python.org").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

nav_tag = soup.find("div")
# print(nav_tag)
navi_item = soup.find_all(id=re.compile("mainnav"))
navigations_tag = soup.find_all(class_=re.compile("tier-1 element-1 with-supernav"))
# navigation = soup.select("ul.python-navigation")
print(navigations_tag)
