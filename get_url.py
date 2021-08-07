import requests
import time
from lxml import etree
from bs4 import BeautifulSoup

root_url = 'https://doupocangqiong1.com/1/list_piaotian/'
def get_url(root_url):
    zhangjie_url = []
    zhangjie_name = []
    res = requests.get(root_url)
    page_source = res.content.decode()
    soup = BeautifulSoup(page_source, 'html.parser')
    # zhangjie = soup.find(name='ul',attrs={'class': {'dirlist three clearfix'}})
    # for item in zhangjie.descendants:
    #     print(item)
    div = soup.find(name='div', class_='card mt20 fulldir')
    body = div.find('div', class_='body')
    ul = body.find('ul')
    for a in ul.find_all('a'):
        zhangjie_url.append(a.get('href'))

    for a in ul.find_all('a'):
        zhangjie_name.append(a.text)
    return zhangjie_url,zhangjie_name

if __name__ == '__main__':
    root_url = 'https://doupocangqiong1.com/1/list_piaotian/'
    print(get_url(root_url))