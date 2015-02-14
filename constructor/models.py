#-*- coding: utf8 -*-
from django.db import models

# Create your models here.
class Email(models.Model):
    class Meta:
        db_table = 'Emails'
        verbose_name = 'Созданное письмо'
        verbose_name_plural = 'Созданные письма'

    email_template = models.ForeignKey('Template')
    title = models.TextField()
    text = models.TextField()
    multimedia_link = models.URLField()

class Template(models.Model):
    class Meta:
        db_table = 'Templates'
        verbose_name = 'Шаблон письма'
        verbose_name_plural = 'Шаблоны писем'

    name = models.CharField(max_length=200)
    html = models.TextField()


class Image(models.Model):
     class Meta:
        db_table = 'Images'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

     image = models.ImageField(upload_to='email_images')

class EmailToImage(models.Model):
    class Meta:
        db_table = 'EmailToImage'
        verbose_name = 'Письмо к изображению'
        verbose_name_plural = 'Письма к изображениям'
    email = models.ForeignKey(Email)
    image = models.ForeignKey(Image)

