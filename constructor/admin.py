from django.contrib import admin
from models import Template, Location, Company, CompanyGroup

# Register your models here.
class TemplateAdmin(admin.ModelAdmin):
    fields = ['name', 'html', 'template']

class CompanyInline(admin.StackedInline):
    model = Company

class CompanyGroupInline(admin.StackedInline):
    model = CompanyGroup

class LocationAdmin(admin.ModelAdmin):
    inlines = [
        CompanyInline,
    ]

    fields = ["name"]

class CompanyAdmin(admin.ModelAdmin):
    fields = ['company_name', 'location']

class CompanyGroupAdmin(admin.ModelAdmin):
    inlines = [
        CompanyInline,
    ]
    fields = ['name']

admin.site.register(Template, TemplateAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyGroup, CompanyGroupAdmin)