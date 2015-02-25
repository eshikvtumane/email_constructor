#-*- coding: utf8 -*-
import json, datetime
import os
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from django import template
from constructor import models
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from sets import Set
import bleach
from utils import clear_tmp

from email_sender.models import Shedule

from django.contrib.sites.models import get_current_site
# Create your views here.



class ConstructorEmailView(View):
    template = 'email_constructor.html'
    def get(self, request):
        args = {}
        args['groups'] = models.CompanyGroup.objects.all()
        args['companies'] = models.Company.objects.all()
        args['locations'] = models.Location.objects.all()
        # получаем путь до шаблонов
        args['templates'] = models.Template.objects.all().values('name',
                                                                 'id',
                                                                 'html',
                                                                 'thumbnail')
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
class TemplateRenderPreview(View):
    def post(self, request):
        tr = TemplateRenderer(request=request, dir='/media')

        template_render = tr.websiteParameters(request, 'tmp', 'image')
        return HttpResponse(template_render)




class TemplateRenderer():

    '''-----------------------------------------------------------
        websiteParameters
    -----------------------------------------------------------'''
    def __init__(self, request, dir=''):
         self.url = 'http://' + get_current_site(request).domain + dir
         print  self.url


    def websiteParameters(self, request, dir, imgs_name):
        method_obj = request.POST
        if(request.method != 'POST'):
            method_obj = request.GET

        link = {
            'path': self.url,
            'dir': dir
        }


        arr = self.savingImg(request.FILES.getlist(imgs_name), **link)
        param, texts = self.requestParameters(method_obj, request.FILES, **link)


        file = self.generateTemplate(param, texts, arr)
        return file

# сохранение изображений на сервер
    def savingImg(self, files, dir = 'tmp', path=settings.MEDIA_URL):
        arr_path = []
        for image in files:
            original_name, file_extension = os.path.splitext(image.name)

            filename = original_name + '-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + file_extension

            save_path = default_storage.save(os.path.join(dir, filename), ContentFile(image.read()))
            image_url = os.path.join(path, save_path)
            arr_path.append(image_url)
        return arr_path


    # работаю с параметрами, которые приходят с сервера, в одном месте
    def requestParameters(self, request_method, files, dir='', path=''):
        template_id = request_method.get('temp_id')
        subject = request_method.get('subject')
        footer = request_method.get('footer')
        social_btn = request_method.get('social_buttons')

        bg_color = request_method.get('background-color')
        header_color = request_method.get('head_background-color')

        fixed_bg = request_method.get('fixed_bg')
        texts = request_method.getlist('text')
        from_email = request_method.get('address')

        args = {
            'email_template': template_id,
            'subject': subject,
            'footer': footer,
            'from_email': from_email,
            'domain_name': self.url
        }

        bg_img_list = files.getlist('background-image')
        if(bg_img_list):
            bg_img = self.savingImg(bg_img_list, dir, path)
            args['bg_img'] = bg_img[0]

        if(bg_color):
            args['bg_color'] = bg_color
        if(header_color):
            args['header_color'] = header_color

        header_img_list = files.getlist('head_background-image')
        if(header_img_list):
            header_img = self.savingImg(header_img_list, dir, path)
            args['header_img'] = header_img[0]

        # социальные кнопки
        if social_btn == 'on':
            social_obj = models.Social.objects.all()
            for s in social_obj:
                s.icon = '/'.join([path, s.icon.name])

                args['social_buttons'] = social_obj
        if social_btn == u'true':
            args['social_buttons'] = 'on'

        return args, texts


    '''
    -----------------------------------------------------------------
        generateTemplate
    ----------------------------------------------------------------------
    '''
    def generateTemplate(self, param, texts, imgs):
        t = models.Template.objects.all().get(id=param['email_template']).template
        template_obj = get_template(t)

# добавление текста в шаблон
        text_count = 1
        for text in texts:
            key = 'text' + str(text_count)
            param[key] = text
            text_count += 1

# Добавление путей к изображениям
        image_path = imgs
        image_count = 1
        for img in image_path:
            img_key = 'image' + str(image_count)
            param[img_key] = img
            image_count += 1

        c = Context(param)
        return template_obj.render(c)



# изменение фона в тех блоках, где необходимо выбрать между изображением и цветом
    def __backgroundStyle(self,files, color, img_name, key_color, key_image):
        args = {}
        img = files.getlist(img_name)
        if color:
            args[key_color] = color
        if img:
            image_path = self.savingImg(img, 'tmp')
            args[key_image] = image_path[0]
        return args



# сохранение шаблона письма в базу
class SaveTemplateView(View):
    def post(self, request):
        try:
            tr = TemplateRenderer(request)
            param, texts = tr.requestParameters(request.POST, request.FILES, 'email_images')

            locations = json.loads(request.POST.get('locations'))
            groups = json.loads(request.POST.get('groups'))
            users = json.loads(request.POST.get('users'))

        # переводим дату и время из строки в объект
            str_datetime = request.POST.get('datetime')
            sheduled_date = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M')

# добавление времени отправки к параметрам
            param['sheduled_time'] = str_datetime

            # получение объекта шаблона
            param['email_template'] = models.Template.objects.get(pk=param['email_template'])

            # сохранение параметров письма
            email_obj = models.Email.objects.create(**param)


            # добавление текста из шаблона
            text_objs = [models.Text(email= email_obj, text = text) for text in texts]


            # сохранение текста из шаблона
            models.Text.objects.bulk_create(text_objs)

    # добавление местопложения, групп пользователей и компаний
            usr_locations = models.Company.objects.filter(location__in = locations)
            usr_groups = models.Company.objects.filter(group__in = groups)
            users_obj = models.Company.objects.filter(id__in=users)

            tuple_users_id = Set()
            usr_total = list(usr_locations) + list(usr_groups) + list(usr_locations)

            for i in usr_total:
                tuple_users_id.add(i)

            users_id = list(tuple_users_id)
            email_obj.users.add(*users_id)
            email_obj.save()


    # добавление картинки
            images_path = tr.savingImg(request.FILES.getlist('images'), 'email_images')
            images_list = [models.Image(email = email_obj, picture = path) for path in images_path]

            models.Image.objects.bulk_create(images_list)

    # добавление задачи в расписание
            #sh = Shedule(email = email_obj, datetime = datetime_format)
            #sh.save()

            return HttpResponse('200', 'text/plain')

        except Exception as e:
            return HttpResponse('500 ' + e.message, 'text/plain')



# формирование шаблона по данным из БД
class DatabaseGenerateTemplate(TemplateRenderer):
    def __init__(self, email_id):
        self.dir = '/media'
        self.email_id = email_id
        self.email_obj = models.Email.objects.get(pk=email_id)

    def getEmailParameters(self):
        """ Получнение адресов для рассылки"""
        email_obj = self.email_obj
        emails_list = email_obj.users.values('company_email')
        emails = [ d['company_email'] for d in emails_list]

        subject = email_obj.subject
        from_email = email_obj.from_email
        print emails_list
        return emails, subject, from_email


    def databaseTemplate(self):
        email_id = self.email_id
        email_obj = self.email_obj


        email_param = self.valueToDict(email_obj)

        texts_dict = models.Text.objects.filter(email=email_obj).values('text')
        texts = [t['text'] for t in texts_dict]

        imgs_dict = models.Image.objects.filter(email=email_obj).values('picture')
        imgs = [ email_param['domain_name']+img['picture'] for img in imgs_dict]
        template = self.generateTemplate(email_param, texts, imgs)

        return template

    def valueToDict(self, email_obj):
        template_id = email_obj.email_template.id
        subject = email_obj.subject
        footer = email_obj.footer
        social_btn = email_obj.social_buttons

        bg_color = email_obj.bg_color
        header_color = email_obj.header_color

        from_email = email_obj.from_email

        args = {
            'email_template': template_id,
            'subject': subject,
            'footer': footer,
            'from_email': from_email,
            'domain_name': email_obj.domain_name
        }

        bg_img = email_obj.bg_img.name
        if(bg_img):
            bg_img = os.path.join(email_obj.domain_name, 'media', bg_img)
            args['bg_img'] = bg_img
            print args['bg_img']

        if(bg_color):
            args['bg_color'] = bg_color
        if(header_color) :
            args['header_color'] = header_color


        header_img = email_obj.header_img.name
        if(header_img):
            header_img = os.path.join(email_obj.domain_name, 'media', header_img)
            args['header_img'] = header_img

        # социальные кнопки
        if social_btn == 'on':
            social_obj = models.Social.objects.all()
            for s in social_obj:
                s.icon = '/'.join([email_obj.domain_name, 'media', s.icon.name])

            args['social_buttons'] = social_obj
        return args

