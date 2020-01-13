from celery import shared_task
import time

# #app = Celery('app_tasks', broker=r"pyamqp://gmcsiwpn:D8hm-ZEVOkEmJ_jWp9PBvPwDUXTOeO6x@shark.rmq.cloudamqp.com/gmcsiwpn")

@shared_task()
def add(x, y):
    #simulate a long runnig process here. It can be a huge computation, calls to external APIs, DB Operations, etc
    time.sleep(15)
    return x + y