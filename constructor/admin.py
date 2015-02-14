from django.contrib import admin
from models import Template

# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
    fields = ['name', 'html', 'template']

admin.site.register(Template, TemplateAdmin)
