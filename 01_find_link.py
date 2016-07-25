import urllib.request
from bs4 import BeautifulSoup


def find_link(target_url):
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


target_url = 'http://search.sina.com.cn/?ie=utf-8&q=%E5%AE%8B%E4%BB%B2%E5%9F%BA&c=news&page=1'
find_link(target_url)
