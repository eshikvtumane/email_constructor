from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'email_constructor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^constructor/', include('constructor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
#http://stackoverflow.com/questions/16196603/images-from-imagefield-in-django-dont-load-in-template
#https://docs.djangoproject.com/en/dev/howto/static-files/#deploying-static-files-in-a-nutshell
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)