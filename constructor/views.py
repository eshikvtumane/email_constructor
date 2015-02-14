from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext
from django.http import HttpResponse
from django import template
from constructor import models


# Create your views here.

class ConstructorEmailView(View):
    template = 'email_constructor.html'
    def get(self, request):
        args = {}

        return render_to_response(self.template, RequestContext(request, args))



class FirstTemplateView(View):
    template = 'template_1.html'
    def get(self, request):
        args = {}

        return render_to_response(self.template, RequestContext(request, args))


class TemplateRenderer(View):
    def get(self,request):
        t = list( models.Template.objects.filter(id=1))[0]
        template_obj = template.Template(t.html)
        args = {'title': 'Hello','message':'Hello dude!'}
        c = RequestContext(request,args)
        return HttpResponse(template_obj.render(c))