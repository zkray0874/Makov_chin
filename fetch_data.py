# coding=utf8
from bs4 import BeautifulSoup
import requests
import sys
import re
"""Fetch song lyrics from 魔鏡歌詞網https://mojim.com only and return a clean text of the song lyrics """


def dep(text):
    unicode = text.prettify().encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return unicode


def de(text):
    unicode = text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)
    return unicode


def get_data():

    url = input('請輸入歌詞網址(魔鏡歌詞網https://mojim.com限定):')

    pat2 = re.compile(r'https://mojim.com/twy.+')
    while re.match(pat2, url) == None:
        print('打錯網址了,小王八蛋')
        url = input('請輸入歌詞網址(魔鏡歌詞網https://mojim.com限定):')

    else:

        soure = requests.get(url).text

        soup = BeautifulSoup(soure, 'lxml')

        text = str(soup.find('dd', id='fsZx3', class_='fsZx3'))

        pat = re.compile(r'<br/>')
        pat1 = re.compile(r'更多更詳盡歌詞 在 <a href="http://mojim.com">※ Mojim.com　魔鏡歌詞網 </a>|<.*>|\[.*|.*：.*')
        lrc = re.sub(pat, '\n', text)
        lrc = re.sub(pat1, '', lrc)
        lrc = lrc.strip()
        return(lrc)



