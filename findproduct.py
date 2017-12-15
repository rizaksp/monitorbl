import requests, sys
from bs4 import BeautifulSoup as BS

if len(sys.agrs) != 2:
    sys.exit()

def Main(url='https://bukalapak.com'):
    r = requests.get(url)
    html = BS(r.text)
    l_prods = html.select('.product__name')

    url_local = 'http://127.0.0.1/link/init?urlp={}&title={}'
    for l in l_prods:
        hre = p.attrs.get('href')
        ttl = p.attrs.get('title')
        try :
            requests.get(url_local.format(hre, ttl))
        except :
            pass


if __name__ == '__main__':
    Main()
