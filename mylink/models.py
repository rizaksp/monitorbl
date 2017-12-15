# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MyLink(models.Model):
    nama_lapak = models.CharField(max_length=200, unique=True)
    urlp = models.CharField(max_length=200)
    terjual = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)
    toko = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nama_lapak

    def url(self):
        return 'https://bukalapak.com'+self.urlp