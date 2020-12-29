import requests
from bs4 import BeautifulSoup

req = requests.get('https://finance.naver.com/sise/')

html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_stock = soup.select(
    '.lst_pop'
)

for stock_name in my_stock:
    print(stock_name.text)