import requests
from bs4 import BeautifulSoup as bs
html = requests.get('https://live.skillbox.ru/')

print(html.status_code)

soup = bs(html.content, features='html.parser')
print(len(soup))