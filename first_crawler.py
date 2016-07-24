import urllib.request
from bs4 import BeautifulSoup
target_url = 'http://search.sina.com.cn/?q=%BA%AB%D0%C7&range=all&c=news&sort=time'

URL = target_url
res = urllib.request.urlopen(URL)
html = res.read()
soup = BeautifulSoup(html, 'html.parser')
result = soup.find('div', class_='result')
lists = result.find_all('div', class_='box-result clearfix')
for list in lists:
    link = list.find('a')
    print(link['href'])
    print(link.get_text())
    media = list.find('span', class_='fgray_time')
    print(media.get_text())

