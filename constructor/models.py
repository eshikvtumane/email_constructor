#-*- coding: utf8 -*-
from django.db import models
# from email_sender import listeners

# Create your models here.
class Email(models.Model):
    class Meta:
        db_table = 'Emails'
        verbose_name = 'Созданное письмо'
        verbose_name_plural = 'Созданные письма'

    email_template = models.ForeignKey('Template')
    subject = models.CharField(max_length=255)

    # цвет фона
    bg_color = models.CharField(max_length=6, blank=True, null=True)
    #изображение для фона
    bg_img = models.FileField(upload_to='email_images', blank=True, null=True)

    # цвет фона header'а
    header_color = models.CharField(max_length=6, blank=True, null=True)
    # изображение для фона header'а
    header_img = models.FileField(upload_to='email_images', blank=True, null=True)

    # фон footer'а
    footer = models.CharField(max_length = 6, blank=True, null=True)
    social_buttons = models.CharField(max_length=6, blank=True, null=True)


    users = models.ManyToManyField('Company', blank=True, null=True)


    sheduled_time = models.DateTimeField(blank=True)
    from_email = models.CharField(max_length = 255)
    domain_name = models.TextField()

    task_id = models.CharField(max_length=256, blank=True, null=True)


# модель для хранения текстов, содержащихся в письме
class Text(models.Model):
    class Meta:
        db_table = 'Texts'
        verbose_name = 'Текст в письме'
        verbose_name_plural = 'Тексты в письмах'

    email = models.ForeignKey('Email')
    text = models.TextField()


class Template(models.Model):
    class Meta:
        db_table = 'Templates'
        verbose_name = 'Шаблон письма'
        verbose_name_plural = 'Шаблоны писем'

    name = models.CharField(max_length=200)
    html = models.FileField(upload_to='html_templates')
    template = models.FileField(upload_to='html_templates')
    thumbnail = models.FileField(upload_to="thumbnails")

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return self.company_name


# Местоположение полователя
class Location(models.Model):
    class Meta:
        db_table = 'Locations'
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Social(models.Model):
    class Meta:
        db_table = 'Socials'
        verbose_name = 'Ссылка на соц. сеть'
        verbose_name_plural = 'Ссылки на соц. сети'

    name = models.CharField(max_length=30)
    link = models.TextField()
    icon = models.FileField(upload_to='social_icons')


#######SIGNALS##############
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
import celery
from email_sender import tasks


def email_handler(*args, **kwargs):
    instance = kwargs.get('instance')
    send_email = False
    print '='*40
    print instance.pk
    print '='*40
    # try:
    #     obj = Email.objects.get(pk=instance.pk)
    #     if obj.sheduled_time != instance.sheduled_time:
    #         send_email = True
    # except Email.DoesNotExist:
    #     obj = instance
    #     send_email = True
    #
    # if send_email:
    #     if obj.task_id:
    #         # Если задача уже в shedule, то удаляем её оттуда
    #         celery.task.control.revoke(obj.task_id)
    #
    #     result = tasks.send_email.apply_async(eta=instance.sheduled_time, kwargs={
    #         'email_id':instance.pk})
    #
    #     instance.task_id = result.task_id

    id = instance.pk
    result = tasks.send_email.apply_async((id,), eta=instance.sheduled_time)
    print "Task id"
    print result.task_id
    #print result.stat
    instance.task_id = result.task_id

post_save.connect(email_handler, sender=Email)