from django.contrib import admin
from models import Template, Location, Company, CompanyGroup, Email, Image, Color

# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
    fields = ['name', 'html', 'template']

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
        ImageInline
    ]
    fields = ['email_template', 'subject', 'title', 'text', 'multimedia_link', 'footer', 'users', 'from_email']

class ColorAdmin(admin.ModelAdmin):
    fields = [ 'email', 'color']

admin.site.register(Template, TemplateAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyGroup, CompanyGroupAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Color, ColorAdmin)