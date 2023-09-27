import requests
import re
from bs4 import BeautifulSoup

# https://intl.cmf.tech/pages/watch-pro
web_site_html_text = requests.get("https://www.python.org/psf-landing/").text
soup = BeautifulSoup(web_site_html_text, "html.parser")

content = soup.find('div#content')
print(content)
# for text in content.find('h1[style=]"text-algin: center; color: #666666;"]'):
#     print(text.text)
# print(content.find_all("h1[style="'text-align: center; color: #666666;']))

a_tag = soup.find('a')
print(a_tag.get('href'))
grants = soup.find(string=re.compile('Grants'))
print(grants)
jobs = set()
for job in soup.body.ul('li'):
    jobs.add(f'{job.a.string})')
print(jobs)
# # print()
# # h2 tagのものを取得する
# for job in soup.body.section('h2'):
#     jobs.add(f'{job.a.string}) ({job.a["href"]}')

# str.lowerでabc順に表示しますよーというオプションです
# print('\n'.join(sorted(jobs, key=str.lower)))
# # print(web_site_html_text)
