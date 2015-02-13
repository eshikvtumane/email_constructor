#-*- coding: utf8 -*-
from django.db import models

# Create your models here.
class Email(models.Model):
    class Meta:
        db_table = 'Emails'
        verbose_name = 'Созданное письмо'
        verbose_name_plural = 'Созданные письма'

    email_template = models.ForeignKey('Template')
    subject = models.CharField(max_length=255)
    title = models.TextField()
    text = models.TextField()

    multimedia_link = models.TextField()
    footer = models.TextField()


    users = models.ManyToManyField('Company', blank=True, null=True)

    from_email = models.CharField(max_length = 255)


class Template(models.Model):
    class Meta:
        db_table = 'Templates'
        verbose_name = 'Шаблон письма'
        verbose_name_plural = 'Шаблоны писем'

    name = models.CharField(max_length=200)
    html = models.FileField(upload_to='html_templates')
    template = models.FileField(upload_to='html_templates')


class Image(models.Model):
    class Meta:
        db_table = 'Images'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    email = models.ForeignKey('Email')
    picture = models.ImageField(upload_to='email_images')

# компании по группам
class CompanyGroup(models.Model):
    class Meta:
        db_table = 'CompanyGroups'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    name = models.CharField(max_length=100)


# компании
class Company(models.Model):
    class Meta:
        db_table = 'Companies'
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

    group = models.ForeignKey('CompanyGroup')
    location = models.ForeignKey('Location')
    company_name = models.TextField()

    company_email = models.CharField(max_length=254)

# Местоположение полователя
class Location(models.Model):
    class Meta:
        db_table = 'Locations'
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    name = models.CharField(max_length=100)

