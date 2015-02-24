#-*- coding: utf8 -*-
from tasks import send_email
from django.db.models.signals import pre_save
from constructor.models import Email
import celery


def email_handler(*args, **kwargs):
    instance = kwargs.get('instance')
    send_email = False
    try:
        obj = Email.objects.get(pk=instance.pk)
        if obj.datetime != instance.datetime:
            send_email = True
    except Email.DoesNotExist:
        obj = instance
        send_email = True

    if send_email:
        if obj.task_id:
            # Если задача уже в shedule, то удаляем её оттуда
            celery.task.control.revoke(obj.task_id)

        result = send_email.apply_async(eta=instance.datetime, kwargs={'pk':
                                                                       instance.pk})
        instance.task_id = result.task_id

pre_save.connect(email_handler, sender=Email)