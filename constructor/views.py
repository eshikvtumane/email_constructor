#-*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponse
import json

from django.contrib.auth.models import Group, User


# Create your views here.

class ConstructorEmailView(View):
    template = 'email_constructor.html'
    def get(self, request):
        args = {}
        args['groups'] = Group.objects.all();
        return render_to_response(self.template, RequestContext(request, args))

# поиск пользователей по введённым буквам
class SearchUserAjax(View):
    def get(self, request):
        enter_word = request.GET.get('s_word')
        result_search = list(User.objects.filter(username__contains = enter_word).values('id', 'username'))
        send_json = json.dumps(result_search)
        return HttpResponse(send_json, content_type='application/json')
