import colorama
colorama.init()
from requests import get
url = 'http://wttr.in/Saint_Petersburg'
x = get(url)
print(x.text)