#-*- coding: utf8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from constructor.models import Email, Template, Image, Text
from django.http import HttpResponse
from constructor.tempate_generator import DatabaseGenerateTemplate



# Create your views here.

def send_email(request, email_id):
    email_id = int(email_id)
    # получение объкта выбранного письма
    dgt = DatabaseGenerateTemplate(email_id)
    email_template = dgt.databaseTemplate()
    email_list, subject, from_email = dgt.getEmailParameters()
    #send(subject,from_email,email_template,email_list)
    return HttpResponse('200',content_type='text/plain')

