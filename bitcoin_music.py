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


    elems = soup.select("#btc_jpy_top_bid")
    for elem in elems:
        data.append(elem.getText())
        #print(elem.getText())
    data[i] = data[i].replace(",","")
    data[i] = float(data[i])
    data[i] = round(data[i])
    rhythm = data[i] - data[i-1]
    
    t = np.linspace(0, np.pi*2*(500+rhythm/10), 44100)
    y = np.sin(t)
    IPython.display.display(IPython.display.Audio(data=y, rate=44100))
    #print(data)
    print(rhythm)
    sleep(3)