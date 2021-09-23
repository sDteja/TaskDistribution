from celery import Celery
from celery.utils.log import get_task_logger

celery_app = Celery('tasks', broker='pyamqp://guest@rabbit//')
logger = get_task_logger(__name__)


@celery_app.task
def add(x, y):
    res = x+y
    logger.info("res : {}".format(res))
    return res

