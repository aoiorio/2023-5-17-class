# 1
print(1)
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





