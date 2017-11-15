from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.Inicio, name='Home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^photos', views.photos, name='photos'),
    url(r'^thanks', views.thanks, name='thanks'),
    ]