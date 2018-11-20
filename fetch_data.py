# coding=utf8
from bs4 import BeautifulSoup
import requests
import sys
import re


def dep(text):
    unicode = text.prettify().encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return unicode


def de(text):
    unicode = text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return unicode


# url = input('請輸入歌詞網址(魔鏡歌詞網https://mojim.com限定):')
soure = requests.get('https://mojim.com/twy100951x22x3.htm').text

soup = BeautifulSoup(soure, 'lxml')
# print(dep(soup))
text = str(soup.find('dd', id='fsZx3', class_='fsZx3'))
# print(text)
pat = re.compile(r'<br/>')
pat1 = re.compile(r'更多更詳盡歌詞 在 <a href="http://mojim.com">※ Mojim.com　魔鏡歌詞網 </a>|<.*>|\[.*|.*：.*')
lrc = re.sub(pat, '\n', text)
lrc = re.sub(pat1, '', lrc)
lrc = lrc.strip()

print(lrc)
