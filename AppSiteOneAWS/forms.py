# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
    
class ContactForm(forms.Form):
    nome = forms.CharField()
    assunto = forms.CharField(required=True)
    correio = forms.EmailField(required=True)
    mensagem = forms.CharField(widget=forms.Textarea)