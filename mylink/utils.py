import requests
from bs4 import BeautifulSoup as BS

def updateData(list_data):
    for d in list_data:
        try :
            r = requests.get(d.url())
            html = BS(html.text)

            text_terjual = html.select('.qa-pd-sold-value')[0].text
            text_price = html.select('.c-product-detail-price')[0].attrs.get('data-reduced-price')
            text_penjual = html.select('.c-user-identification__name')[0].text

            count = int(text_penjual.strip().replace('.',''))
            price = int(text_price.strip().replace('.',''))
            penjual = text_penjual.strip()

            d.terjual = count
            d.harga = price
            d.toko = penjual
        except:
            pass
        
        finally :
            d.save()