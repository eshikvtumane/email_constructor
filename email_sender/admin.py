from django.contrib import admin
import models

# Register your models here.
class SheduleAdmin(admin.ModelAdmin):
    fields = [ 'email', 'datetime' ]

admin.site.register(models.Shedule, SheduleAdmin)