#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from views import ConstructorEmailView, SearchUserAjax

from views import ConstructorEmailView,FirstTemplateView,TemplateRenderer, TemplateLoadAjax


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'email_constructor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^email_templates/$', ConstructorEmailView.as_view(), name='email_templates'),

# поиск пользователей
    url(r'^search_users/$', SearchUserAjax.as_view()),
# загрузка выбранного шаблона
    url(r'^template_load/(?P<id>[0-9]+)/$', TemplateLoadAjax.as_view()),

    url(r'^render_template/$', TemplateRenderer.as_view(), name='render_template' ),
)
