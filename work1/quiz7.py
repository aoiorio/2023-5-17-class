import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
}
# web_site_html_text = requests.get("https://www.livedoor.com/201401/topics/11.inc?t=1695955762477").content
text = requests.get(
    "https://news.yahoo.co.jp/topics", headers=headers
).content


soup = BeautifulSoup(text, 'html.parser')

news = soup.find_all("a", class_="sc-dtLLSn dpehyt")
# print(news)

for title in news:
    print(title.text)