#-*- coding: utf8 -*-
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context

from django.core.mail import EmailMultiAlternatives
from constructor.models import Email, Template, Image

# Create your views here.

def email_send(request, email_id):
    id = email_id
    # получаем письмо, которое необходимо отправить
    email_parameters = Email.objects.get(pk=id)

    # получаем ссылку на шаблон
    email_template = Template.objects.all().get(pk=email_parameters.email_template).template

    html = get_template(email_template)
    args = {
        'title': email_parameters.title,
        'text': email_parameters.text,
        'video': email_parameters.multimedia_link
    }
# получаем изображения для письма
    images = Image.objects.filter(id=email_parameters).values('picture')
    img_count = 1
    for img in images:
        key = 'image' + str(img_count)
        args[key] = img['picture']
        img_count += 1

    companies = email_parameters.users.all()
    print companies

    groups = email_parameters.groups.all().values('groups__')
    locations = email_parameters.locations.all()


# генератор шаблона
    content = Context(args)
# генерация простого текста на случай, есди просмоторщик не сможет распознать наше письмо
    #text_content = plaintext.render(content)
    text_content = 'Hello'
# генерация html письма
    html_content = html.render(content)


    subject = email_parameters.subject
    from_email = email_parameters.from_email
    to = []
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    #msg.send()


def test():
    print 2+2
