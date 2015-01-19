# -*-coding: utf-8-*-

from celery import Celery
from op import utils
import celeryconfig


worker = Celery('Regular-Ticket-Task')
worker.config_from_object(celeryconfig)
worker.conf.BROKER_URL = utils.get_config('celery', 'BROKER_URL')
worker.conf.CELERY_RESULT_BACKEND = utils.get_config('celery', 'CELERY_RESULT_BACKEND')
