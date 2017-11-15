# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render, render_to_response, redirect
from django.template.response import TemplateResponse
from django.utils import timezone

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import ContactForm
from .models import Question

def Inicio (request):
    return render (request, 'home.html')

def contact (request):
    Mystring = timezone.now
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nome']
            subject = form.cleaned_data['assunto']
            from_email = form.cleaned_data['correio']
            message = form.cleaned_data['mensagem']
            try:
                send_mail(subject,
                    message,
                    from_email,
                    ['djangotests123@gmail.com', from_email],
                    fail_silently=False)      
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')        
    return render (request, 'basicContacts.html',{'content':['Pode o usar o endereço: XPTO_11@outlook.com', 'ou prencher o formulário a seguir', Mystring]})

def blog (request):
    return render(request, 'blog.html')

def photos (request):
    return render(request, 'photos.html')

def experimentar(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['nome']
            subject = form.cleaned_data['assunto']
            from_email = form.cleaned_data['correio']
            message = form.cleaned_data['mensagem']
            try:
                send_mail(subject,
                    message,
                    from_email,
                    ['djangotests123@gmail.com', from_email],
                    fail_silently=False)      
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return HttpResponseRedirect(reverse('app_name:thanks'))    
    return render(request, "basicToexperimentar.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')
