#-*- coding: utf8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from constructor.models import Email, Template, Image


# Create your views here.

def email_send(request, email_id):
    id = email_id
    # получаем письмо, которое необходимо отправить
    email_parameters = Email.objects.get(pk=id)

    # получаем ссылку на шаблон
    email_template = Template.objects.get(id=email_parameters.email_template.id).template

    html = get_template(email_template)
    args = {
        'title': email_parameters.title,
        'text': email_parameters.text,
        'video': email_parameters.multimedia_link
    }
# получаем изображения для письма
    images = Image.objects.filter(email=email_parameters).values('picture')
    print images
    img_count = 1
    for img in images:
        key = 'image' + str(img_count)
        print img['picture']
        args[key] = img['picture']
        img_count += 1

    print args

# Получнение адресов для рассылки
    emails_list = email_parameters.users.values('company_email')
    emails = [ d['company_email'] for d in emails_list]

    print email_parameters.users.values('company_name')
    print emails
# генератор шаблона
    content = Context(args)
# генерация простого текста на случай, есди просмоторщик не сможет распознать наше письмо
    #text_content = plaintext.render(content)
    text_content = 'Hello'
# генерация html письма
    html_content = html.render(content)


    subject = email_parameters.subject
    from_email = email_parameters.from_email
    to = emails
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    #msg.send()

    send_mail(subject, html_content, from_email, to, fail_silently=False)

