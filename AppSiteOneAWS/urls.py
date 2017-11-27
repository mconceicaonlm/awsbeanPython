# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.views.generic import ListView, DetailView
from . import views
from .models import Produtos

urlpatterns = [
    url(r'^$', views.Inicio, name='Home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^photos', views.photos, name='photos'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^(?P<Produtos>[0-9]+)/$', views.details, name='Produtos'),
    # url(r'^(?P<imagem>[0-9]+)/results/$', views.details, name='result'),
    url(r'^Produtos', ListView.as_view(queryset = Produtos.objects.all().order_by("prodnome")[:25],
                                                    template_name="produtos.html")),
    # url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Produtos, template_name = 'detalheprodutos.html'))
    ]