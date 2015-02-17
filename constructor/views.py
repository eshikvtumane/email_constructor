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
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings



# Create your views here.

class ConstructorEmailView(View):
    template = 'email_constructor.html'
    def get(self, request):
        args = {}
        args['groups'] = models.CompanyGroup.objects.all()
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
        image = request.FILES['image']
        save_path = default_storage.save('tmp/somename.jpg', ContentFile(image.read()))
        image_url = os.path.join(settings.MEDIA_ROOT, save_path)

        t = models.Template.objects.all().get(id=template_id).template
        template_obj = get_template(t)

        args = {'title': title,'text':text, 'video':url,'image':image_url}
        c = RequestContext(request,args)

        return HttpResponse(template_obj.render(c))

