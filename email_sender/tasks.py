from celery import task
from celery.task.base import periodic_task
import datetime
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

def test_method():
    return 1+1

@periodic_task(run_every=datetime.timedelta(minutes=5))
def email_sending_method(id=1):
    logger.info("Start task")
    result = test_method()
    logger.info("Task finished: result = %i" % result)

email_sending_method()

