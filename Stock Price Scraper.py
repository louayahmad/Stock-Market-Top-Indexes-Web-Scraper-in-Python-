import bs4
import requests
from bs4 import BeautifulSoup

def getSandP500StockPrice():
    r = requests.get("https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC")
    soup = BeautifulSoup(r.text,"lxml")
    price1 = soup.find_all('div',{'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price1

def getDowStockPrice():
    r = requests.get("https://finance.yahoo.com/quote/%5EDJI?p=^DJI")
    soup = BeautifulSoup(r.text,"lxml")
    price2 = soup.find_all('div',{'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price2

def getNasdaqStockPrice():
    r = requests.get("https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC")
    soup = BeautifulSoup(r.text,"lxml")
    price3 = soup.find_all('div',{'class': 'D(ib) Mend(20px)'})[0].find('span').text
    return price3

while True:
    print("S&P 500 stock Price is " +str(getSandP500StockPrice()))
    print("The Dow stock Price is " +str(getDowStockPrice()))
    print("Nasdaq stock Price is " +str(getNasdaqStockPrice()))
































