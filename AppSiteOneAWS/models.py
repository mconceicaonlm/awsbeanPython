# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

class Produtos(models.Model):
    prodnome = models.CharField(_('Nome'), max_length=50)
    descricao = models.CharField(_('Descricao'), max_length= 200, default ='')
    imagem = models.ImageField(upload_to='produtos/', null=True) 
    imgpequena = models.ImageField(upload_to='produtos/', null=True)
    preco = models.DecimalField('Valor', max_digits=8, decimal_places=2, default=0)
    active = models.BooleanField(_('Ativo'), default=True)
    TotalExistente = models.IntegerField(_('Total Existente'), default=1)
    created_at = models.DateTimeField(  
        _('Criado em'), auto_now_add=True, auto_now=False)
    pub_date = models.DateTimeField('date published')

    class Meta:
        ordering = ['prodnome']

    def __str__(self):
        return self.prodnome

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class BlogAssunto(models.Model):
    blogassunto_text = models.CharField(max_length= 200)
    pub_date=models.DateTimeField('date published')

    def __str__ (self):
        return self.blogassunto_text

class BlogComments (models.Model):
    blogcomments_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.blogcomments_text
