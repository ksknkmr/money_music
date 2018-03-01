import requests
from bs4 import BeautifulSoup
from time import sleep
import IPython
import numpy as np

data = []

url = "https://cc.minkabu.jp/pair/BTC_JPY"

for i in range(10):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"html.parser")

    #ビットコインの価格抽出
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
    rhythm = data[0] - data[-1]
    
    #音声処理
    t = np.linspace(0, np.pi*2*(500+rhythm/10), 44100)
    y = np.sin(t)
    
    #出力
    IPython.display.display(IPython.display.Audio(data=y, rate=44100))
    print(rhythm)
    sleep(3)