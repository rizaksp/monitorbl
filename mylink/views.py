# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_list_or_404
from django.http.response import HttpResponse


from .models import MyLink
# from .utils import updateData

import requests
from bs4 import BeautifulSoup as BS


def index(request):
    link_qs = MyLink.objects.all()
    content = {
        'links': link_qs
    }

    return render(request, 'mylink/index.html', content)

def initAdd(request):
    urlp = request.GET.get('urlp', '')
    title = request.GET.get('title', '')

    print urlp, title

    if urlp != '' and title !='':
        link_exists = MyLink.objects.filter(nama_lapak=title).exists()
        if not link_exists:
            MyLink.objects.create(urlp=urlp, nama_lapak=title)

    return HttpResponse('0')


def updateData(request):
    link_qss = MyLink.objects.filter(harga=0)
    
    # updateData(link_qs)
    for link_qs in link_qss:
        try :
            r = requests.get(link_qs.url())
            html = BS(r.text, 'html.parser')
            
            text_terjual = html.select('.qa-pd-sold-value')[0].text
            text_price = html.select('.c-product-detail-price')[0].attrs.get('data-reduced-price')
            text_penjual = html.select('.c-user-identification__name')[0].text
            
            counter = int(text_terjual.strip().replace('.',''))
            price = int(text_price.strip().replace('.',''))
            penjual = text_penjual.strip()
            
            link_qs.terjual = counter
            link_qs.harga = price
            link_qs.toko = penjual
            
        except:
            pass
        
        finally :
            link_qs.save()

    return HttpResponse('0')