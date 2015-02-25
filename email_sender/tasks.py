#-*- coding: utf8 -*-
from celery import task
from celery.task.base import periodic_task
import datetime
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from constructor.views import DatabaseGenerateTemplate

logger = get_task_logger(__name__)

def test_method():
    return 1+1

#@periodic_task(run_every=datetime.timedelta(minutes=5))
# @periodic_task(crontab(minute='', hour='',))
# def email_sending_method(id=1):
#     logger.info("Start task")
#     result = test_method()
#     logger.info("Task finished: result = %i" % result)
#
# email_sending_method()


@task
def send_email(email_id):
    id = email_id
    # получение объкта выбранного письма
    dgt = DatabaseGenerateTemplate(id)
    email_template = dgt.databaseTemplate()
    email_list, subject, from_email = dgt.getEmailParameters()
    send_email(subject,email_template,from_email,email_list,fail_silently=False)

