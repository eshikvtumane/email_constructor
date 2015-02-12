from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.template import RequestContext


# Create your views here.

class ConstructorEmailView(View):
    template = 'email_constructor.html'
    def get(self, request):
        args = {}

        return render_to_response(self.template, RequestContext(request, args))