import requests
import re
from bs4 import BeautifulSoup

web_site_html_text = requests.get("https://www.livedoor.com/201401/topics/11.inc?t=1695955762477").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

a_tag = soup.find_all("a")

for i in a_tag:
    print(i.text)

