#!/usr/bin/env python
#-*- cording: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from time import sleep
import IPython
import numpy as np
import pygame.mixer
import time

data = []

url = "https://cc.minkabu.jp/pair/BTC_JPY"

    # 音楽ファイルの読み込み
def beepSound(doremi):
    pygame.mixer.music.load(doremi)
    pygame.mixer.music.play(1)
    time.sleep(2)
    pygame.mixer.music.stop()

for i in range(10):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"html.parser")


    elems = soup.select("#btc_jpy_top_bid")
    for elem in elems:
        data.append(elem.getText())
    
    #余分な配列の削除
    if len(data) > 2:
        data.pop(0)
    #取得した文字列の処理
    data[-1] = data[-1].replace(",","")
    data[-1] = float(data[-1])
    data[-1] = round(data[-1])
    rhythm = data[-1] - data[0]
    
    # mixerモジュールの初期化
    pygame.mixer.init()
    
    # 株価の高低差によって音階を変更
    if rhythm <= -501:
        beepSound("sound/do.ogg")
    elif rhythm <= -301 and rhythm > -500:
        beepSound("sound/re.ogg")
    elif rhythm <= -101 and rhythm > -300:
        beepSound("sound/mi.ogg")
    elif rhythm <= -1 and rhythm > -100:
        beepSound("sound/fa.ogg")
    elif rhythm >= 0 and rhythm < 100:
        beepSound("sound/so.ogg")
    elif rhythm >= 101 and rhythm < 300:
        beepSound("sound/ra.ogg")
    elif rhythm >= 301 and rhythm < 500:
        beepSound("sound/si.ogg")
    elif rhythm >= 501:
        beepSound("sound/do_h.ogg")
    
    print("現在のビットコイン：",data[-1],"円")
    print(rhythm)
    sleep(1)