import urllib.request
from bs4 import BeautifulSoup
import re


def read_page(target_url):
    URL = target_url
    res = urllib.request.urlopen(URL)
    html = res.read()
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('div', class_='content')
    text = result.get_text()
    print(text)

target_url = 'http://eladies.sina.com.cn/wzx/2016-07-25/1044/doc-ifxuhuma7455442.shtml'
read_page(target_url)
