from django.conf.urls import patterns, include, url
from views import ConstructorEmailView,FirstTemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'email_constructor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^email_templates/$', ConstructorEmailView.as_view(), name='email_templates'),
    url(r'^first_template/$', FirstTemplateView.as_view(), name='first_template'),
)

#http://stackoverflow.com/questions/16196603/images-from-imagefield-in-django-dont-load-in-template
#https://docs.djangoproject.com/en/dev/howto/static-files/#deploying-static-files-in-a-nutshell
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)