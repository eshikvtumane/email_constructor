#-*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.http import HttpResponse

import json

from django.contrib.auth.models import Group, User

from django import template
from constructor import models
import datetime
from django.conf import settings
import os




# Create your views here.

class ConstructorEmailView(View):
    template = 'email_constructor.html'
    def get(self, request):
        args = {}
        args['groups'] = models.CompanyGroup.objects.all()
        args['companies'] = models.Company.objects.all().values('id', 'company_name')
        args['locations'] = models.Location.objects.all()
        # получаем путь до шаблонов
        args['templates'] = models.Template.objects.all().values('name', 'id')
        return render_to_response(self.template, RequestContext(request, args))


# поиск пользователей по введённым буквам
class SearchUserAjax(View):
    def get(self, request):
        enter_word = request.GET.get('s_word')
        result_search = list(models.Company.objects.filter(company_name__contains = enter_word).values('id', 'company_name'))
        send_json = json.dumps(result_search)
        return HttpResponse(send_json, content_type='application/json')

# загрузка шаблона письма
class TemplateLoadAjax(View):
    def get(self, request, id):
        # получаем файл
        t = models.Template.objects.all().get(id=id).html

        # считываем все строки файла.
        t.open(mode='rb')
        lines = t.readlines()
        t.close()
        return HttpResponse(lines)


class FirstTemplateView(View):
    template = 'template_1.html'
    def get(self, request):
        args = {}

        return render_to_response(self.template, RequestContext(request, args))


class TemplateRenderer(View):
    def post(self,request):
        template_id = request.POST.get('template_id')
        title = request.POST.get('title')
        text = request.POST.get('text')
        url = request.POST.get('video')
        #image = request.FILES['image']
        #print template_id

        t = models.Template.objects.all().get(id=template_id).template
        template_obj = get_template(t)

        args = {'title': title,'text':text, 'video':url}
        c = RequestContext(request,args)
        #print template_obj.render(c)
        return HttpResponse(template_obj.render(c))

class SaveTemplateView(View):
    def post(self, request):
        template_id = request.POST.get('temp_id')
        subject = request.POST.get('subject')
        title = request.POST.get('title')
        text = request.POST.get('text')
        images = request.POST.get('images')
        multimedia = request.POST.get('multi_url')
        footer = request.POST.get('footer')

        locations = json.loads(request.POST.get('locations'))
        groups = json.loads(request.POST.get('groups'))
        users = json.loads(request.POST.get('users'))

        str_datetime = request.POST.get('datetime')
        datetime_format = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M')


        template_obj = models.Template.objects.get(pk=template_id)
        email_obj = models.Email(
            email_template = template_obj,
            subject = subject,
            title = title,
            text = text,
            multimedia_link = multimedia,
            footer = footer
        )

        email_obj.save()

# добавление местопложения, групп пользователей и компаний
        locations_obj = models.Location.objects.filter(id__in = locations)
        groups_obj = models.CompanyGroup.objects.filter(id__in=groups)
        users_obj = models.Company.objects.filter(id__in=users)

        email_obj.locations.add(*locations_obj)
        email_obj.groups.add(*groups_obj)
        email_obj.users.add(*users_obj)

        email_obj.save()


# добавление картинки
        print request.POST.get('images')
        print type(request.POST.get('images'))
        fuv = FileUploadView()
        images_list = fuv.add_image(request, 'email_images', 'email_picture', email_obj)

        models.Image.objects.bulk_create(images_list)

        return HttpResponse('200', 'text.plain')


# загрузка файлов
class FileUploadView():
    def add_image(self, request, UPLOAD_TO, FILENAME, EMAIL_OBJ):
        print request.FILES
        if request.FILES and request.FILES.get('images'):
            return self.__save_file(UPLOAD_TO,
                             request.FILES.getlist('images'),
                             FILENAME,
                             EMAIL_OBJ)


        return []

    def __save_file(self, dest_path, files, filename, email):
        image_obj = []
        for f in files:
            original_name, file_extension = os.path.splitext(f.name)
            filename = filename + '-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + file_extension
            url = dest_path + '/' + filename
            path = settings.MEDIA_ROOT + url
            with open(path, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            image_obj.append(models.Image(email = email, picture = path))
        return image_obj