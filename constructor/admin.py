from django.contrib import admin
from models import Template, Location, Company, CompanyGroup, Email, Image, Social, Text

# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
    fields = ['name', 'html', 'template','thumbnail']


class TextInline(admin.StackedInline):
    model = Text

class CompanyInline(admin.StackedInline):
    model = Company

class CompanyGroupInline(admin.StackedInline):
    model = CompanyGroup

class LocationAdmin(admin.ModelAdmin):

    fields = ["name"]

class CompanyAdmin(admin.ModelAdmin):
    fields = ['company_name', 'location', 'company_email']

class CompanyGroupAdmin(admin.ModelAdmin):
    inlines = [
        CompanyInline,
    ]
    fields = ['name']

class ImageInline(admin.StackedInline):
    model = Image

class EmailAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        TextInline
    ]
    fields = []

class SocialAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(Template, TemplateAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyGroup, CompanyGroupAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Social, SocialAdmin)