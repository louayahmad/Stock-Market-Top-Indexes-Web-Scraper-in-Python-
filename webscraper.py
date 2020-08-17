import bs4
import requests
from bs4 import BeautifulSoup

def getSandP500StockPrice():
    r = requests.get("https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC")
    soup = BeautifulSoup(r.text,"lxml")
    price1 = soup.find_all('div',{'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price1

def getFacebookStockPrice():
    r = requests.get("https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch")
    soup = BeautifulSoup(r.text,"lxml")
    price2 = soup.find_all('div',{'class': 'D(ib) Va(m) Maw(65%) Ov(h)'})[0].find('span').text
    return price2

def getTeslaStockPrice():
    r = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch")
    soup = BeautifulSoup(r.text,"lxml")
    price3 = soup.find_all('div',{'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price3

while True:
    print("S&P 500 stock Price is " +str(getSandP500StockPrice()))
    print("Facebook stock Price is " +str(getFacebookStockPrice()))
    print("Tesla stock Price is " +str(getTeslaStockPrice()))
