#-*- coding: utf8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from constructor.models import Email, Template, Image, Text



# Create your views here.

def email_send(request, email_id):

    id = email_id
    # получение объкта выбранного письма
    email_obj = Email.objects.get(pk=id)
    print email_obj

    # получение кртинок
    imgs_links = Image.objects.filter(email=email_obj).values('picture')
    img_list = [ img['picture'] for img in imgs_links]
    print img_list

    # получение текстов
    texts = Text.objects.filter(email = email_obj).values('text')
    text_list = [ t['text'] for t in texts]




# Получнение адресов для рассылки
    emails_list = email_obj.users.values('company_email')
    emails = [ d['company_email'] for d in emails_list]

    print emails


