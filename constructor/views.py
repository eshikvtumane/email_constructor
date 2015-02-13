#-*- coding: utf8 -*-
import json
import os
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from django import template
from constructor import models
import datetime
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from sets import Set

from email_sender.models import Shedule



# Create your views here.

class ConstructorEmailView(View):
    template = 'email_constructor.html'
    def get(self, request):
        args = {}
        args['groups'] = models.CompanyGroup.objects.all()
        args['companies'] = models.Company.objects.all()
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

# генерирование шаблона для предварительного шаблона
class TemplateRenderer(View):
    def post(self,request):
        template_id = request.POST.get('template_id')
        title = request.POST.get('title')
        text = request.POST.get('text')
        url = request.POST.get('video')
        image = request.FILES



        image_path = self.__image_save(request)


        t = models.Template.objects.all().get(id=template_id).template
        template_obj = get_template(t)

        args = {'title': title,'text':text, 'video':url}

        image_count = 1
        for img in image_path:
            img_key = 'image' + str(image_count)
            args[img_key] = img
            image_count += 1
        print args
        c = RequestContext(request,args)
        #print template_obj.render(c)

        return HttpResponse(template_obj.render(c))

    def __image_save(self, request):
        files = request.FILES
        arr_path = []
        for f in files:
            image = files.get(f)
            original_name, file_extension = os.path.splitext(image.name)
            filename = 'tmp_image' + '-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + file_extension
            save_path = default_storage.save(os.path.join('tmp', filename), ContentFile(image.read()))
            image_url = os.path.join(settings.MEDIA_URL, save_path)
            arr_path.append(image_url)
        return arr_path

class SaveTemplateView(View):
    def post(self, request):
        try:
            template_id = request.POST.get('temp_id')
            subject = request.POST.get('subject')
            title = request.POST.get('title')
            text = request.POST.get('text')
            images = request.POST.get('images')
            multimedia = request.POST.get('multi_url')
            footer = request.POST.get('footer')
            address = request.POST.get('address')

            locations = json.loads(request.POST.get('locations'))
            groups = json.loads(request.POST.get('groups'))
            users = json.loads(request.POST.get('users'))

        # переводим дату и время из строки в объект
            str_datetime = request.POST.get('datetime')
            datetime_format = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M')


            template_obj = models.Template.objects.get(pk=template_id)
            email_obj = models.Email(
                email_template = template_obj,
                subject = subject,
                title = title,
                text = text,
                multimedia_link = multimedia,
                footer = footer,
                from_email = address
            )

            email_obj.save()

    # добавление местопложения, групп пользователей и компаний

            usr_locations = list(models.Company.objects.filter(location__in = locations))
            usr_groups = list(models.Company.objects.filter(group__in = groups))
            users_obj = list(models.Company.objects.filter(id__in=users))

            tuple_users_id = Set()

            for usr1, usr2, usr3 in zip(usr_locations, usr_groups, usr_locations):
                tuple_users_id.add(usr1.id)
                tuple_users_id.add(usr2.id)
                tuple_users_id.add(usr3.id)

            users_id = list(tuple_users_id)
            print users_id

            email_obj.users.add(*users_id)

            email_obj.save()


    # добавление картинки
            fuv = FileUploadView()
            images_list = fuv.add_image(request, 'email_images', 'email_picture', email_obj)

            models.Image.objects.bulk_create(images_list)

    # добавление задачи в расписание
            sh = Shedule(email = email_obj, datetime = datetime_format)
            sh.save()

            return HttpResponse('200', 'text/plain')

        except:
            return HttpResponse('500', 'text/plain')




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