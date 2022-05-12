from requests import get
import urllib.request

file = open('dataset_3378_3.txt')
url = str(file.readline())
par = '699991.txt'

while not par[:2] == 'We':
    resp = get(url.strip() + par.strip())
    par = resp.text.strip()
    urllib.request.urlretrieve(url.strip() + par.strip(), 'd:/Downloads/13/' + par)
    #print(resp.text.strip())
print(resp.content)
