from django.contrib import admin
from kombu.transport.django import models as kombu_models
import models

# Register your models here.
class SheduleAdmin(admin.ModelAdmin):
    fields = [ 'email', 'datetime' ]

admin.site.register(models.Shedule, SheduleAdmin)

admin.site.register(kombu_models.Message)