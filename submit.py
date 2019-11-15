#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
import urllib
import json
from urllib.parse import quote
from bs4 import BeautifulSoup

word = '徐丽芳'
url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn=0'
response = urllib.request.urlopen(url)
page = response.read()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
} #定义头文件，伪装成浏览器

soup = BeautifulSoup(page, 'lxml')
tagh3 = soup.find_all('h3',{'class':'t'})

for h3 in tagh3:
    name = h3.next_sibling.next_sibling
    titleDiv = name.find('div')
    if titleDiv != None:
       data = titleDiv.get('data-tools')
       text = json.loads(data)
       title = text['title']
       href = h3.find('a').get('href')
       baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
       real_url = baidu_url.headers['Location']  #得到网页原始地址
       if real_url.startswith('http'):
          print('网页标题: ' + title)
          print('链接: ' + real_url)
          print('-------------------------------------------------------------')


