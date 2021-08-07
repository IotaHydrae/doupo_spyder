#coding:utf-8
import requests
import time
from lxml import etree
from bs4 import BeautifulSoup
import re
import json

def craw(url, bid=1, cid=873531):
    # print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    try:
        # res = requests.get(url=url, headers=headers)
        # res.encoding = 'utf-8'
        # soup = BeautifulSoup(res.text, 'html.parser')
        # book_name = soup.find('div', class_='header line').find('h1').text
        # print(book_name)
        print(bid,cid)
        request_url = 'https://doupocangqiong1.com/novelsearch/chapter/transcode.html'
        data = {
            'siteid' : '0',
            'bid' : bid,
            'cid' : cid
        }
        html = requests.post(request_url, headers=headers, data=data).json()
        print(html)
        html = re.sub(r'</?\w+[^>]*>', '', html['info'])
        # with open('folder/2.txt', 'w') as file:
        #     file.write(html)
        #     file.close()
        return html
    except:
        print('error')





if __name__ == '__main__':
    craw('https://doupocangqiong1.com/1/')