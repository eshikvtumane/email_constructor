#-*- coding: utf8 -*-
from celery import task
from celery.task.base import periodic_task
import datetime
from django.core.mail import EmailMultiAlternatives
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from constructor.tempate_generator import DatabaseGenerateTemplate

logger = get_task_logger(__name__)

#@periodic_task(run_every=datetime.timedelta(minutes=5))
# @periodic_task(crontab(minute='', hour='',))
# def email_sending_method(id=1):
#     logger.info("Start task")
#     result = test_method()
#     logger.info("Task finished: result = %i" % result)
#
# email_sending_method()


@task
def send_email(*args, **kwargs):
    # получение объкта выбранного письма
    email_id = args[0]
    dgt = DatabaseGenerateTemplate(email_id)
    email_template = dgt.databaseTemplate()
    email_list, subject, from_email = dgt.getEmailParameters()
    print email_list, subject, from_email

    #msg = EmailMultiAlternatives('fff', 'ddd', 'df@df.rt', email_list)
    #msg.send()
    #send_email('fff','ggg',from_email,['eshikvtumane@mail.ru'])

