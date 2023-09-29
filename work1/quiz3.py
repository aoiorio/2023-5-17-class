import requests
import re
from bs4 import BeautifulSoup

# 3

print(3)
web_site_html_text = requests.get("https://www.python.org").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

nav = soup.find_all("ul", class_=re.compile("navigation menu"))


test = soup.find("ul", {"aria-label": "Main Navigation"}).findChildren(
    "li", recursive=False
)
for a in test:
    print(a.find("a").text)
