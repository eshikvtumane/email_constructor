#-*- coding: utf8 -*-
from django.db import models
from constructor.models import Email

# Create your models here.
class Shedule(models.Model):
    class Meta:
        db_table = 'Shedules'
        verbose_name = 'Расписание отправки'
        verbose_name_plural = 'Расписание отправок'

    email = models.ForeignKey(Email)
    datetime = models.DateTimeField()

