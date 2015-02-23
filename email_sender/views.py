#-*- coding: utf8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from constructor.models import Email, Template, Image, Text
from django.http import HttpResponse
from constructor.views import DatabaseGenerateTemplate



# Create your views here.

def email_send(request, email_id):

    id = email_id
    # получение объкта выбранного письма
    dgt = DatabaseGenerateTemplate(id)
    email_template = dgt.databaseTemplate()
    email_list = dgt.getEmails()

    print email_list

    return HttpResponse(email_template)

