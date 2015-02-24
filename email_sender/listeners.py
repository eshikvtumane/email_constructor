from tasks import send_email
from django.db.models.signals import pre_save
from constructor.models import Email
import celery


def email_handler(*args, **kwargs):
    instance = kwargs.get('instance')
    send_reminder = False
    try:
        obj = Email.objects.get(pk=instance.pk)
        if obj.datetime != instance.datetime:
            send_reminder = True
    except Email.DoesNotExist:
        obj = instance
        send_email = True

    if send_email:
        # look to see if we have a task_id for this task already.
        if obj.task_id:
            # If we do, lets get rid of this scheduled task
            celery.task.control.revoke(obj.task_id)

        result = send_email.apply_async(eta=instance.datetime, kwargs={'pk':
                                                                       instance.pk})
        instance.task_id = result.task_id
git
pre_save.connect(email_handler, sender=Email)