from yahoo_fin.stock_info import *
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

ticker=input('what ticker are you looking at?')
ticker=ticker.upper()
analyst_info=get_analysts_info(ticker)
growthestimates=float(analyst_info['Growth Estimates'][ticker][4].strip('%'))/100
stats=get_stats(ticker)
epsttm=float(stats['Value'][40])
minrate=0.15
marginsafety=0.33
current_market_price=get_live_price(ticker)

url = 'http://financials.morningstar.com/valuate/current-valuation-list.action?&t=XNAS:'+ticker+'&region=usa&culture=en-US&cur=&adsFlag=true&_=1596015761530'
source = urllib.request.urlopen(url).read()

# Parse the html content

soup = BeautifulSoup(source, "lxml")
table = soup.find("table", attrs={"class": "r_table1 text2"})
df = pd.read_html(str(table))[0]
p_e=df[ticker+' 5Y Avg*'][1]
if p_e=='—':
    print('5y not found using double growth rate')
    p_e=2*growthestimates
p_e=float(p_e)
if p_e>2*growthestimates*100:
    p_e=2*growthestimates*100
futurevalue=epsttm
for i in range(9):
    futurevalue+=futurevalue*growthestimates
futureshareprice=futurevalue*p_e
currentshareprice=futureshareprice
for i in range(9):
    currentshareprice=currentshareprice/(1+minrate)
buyprice=currentshareprice*(1-marginsafety)
print(buyprice)
print(current_market_price)
if buyprice>current_market_price:
    print('buy')
else:
    print('dont buy')
