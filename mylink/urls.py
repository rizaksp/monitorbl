from django.conf.urls import url

from . import views

app_name = 'mylink'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init/$', views.initAdd, name='init'),
    url(r'^update/$', views.updateData, name='update')
]