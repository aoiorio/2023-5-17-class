import requests
from bs4 import BeautifulSoup


web_site_html_text = requests.get('https://www.python.org/jobs').text

soup = BeautifulSoup(web_site_html_text, 'html.parser')

jobs = set()

for job in soup.body.section('li'):
    jobs.add(f'{job.a.string})')

# print()
# h2 tagのものを取得する
# for job in soup.body.section('h2'):
#     jobs.add(f'{job.a.string}) ({job.a["href"]}')

# str.lowerでabc順に表示しますよーというオプションです
# print('\n'.join(sorted(jobs, key=str.lower)))
# print(web_site_html_text)