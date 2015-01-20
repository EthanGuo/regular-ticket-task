# -*- coding: utf-8 -*-

from celery.schedules import crontab
from datetime import timedelta


CELERY_ACCEPT_CONTENT = ['json', 'yaml']
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_INCLUDE = ['tasks']  # celery tasks entry
CELERYBEAT_SCHEDULE = {
    'ticket-task': {
        'task': 'tasks.job_ticket_task',
        'schedule': crontab(minute=0, hour='*/1'),
        #'schedule': timedelta(seconds=60)
    },
}

CELERY_TIMEZONE = 'Asia/Shanghai'
