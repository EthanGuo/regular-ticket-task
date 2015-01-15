# -*-coding: utf-8-*-

from celery import Celery
from lib import configuration
import celeryconfig


worker = Celery('Regular-Ticket-Task')
worker.config_from_object(celeryconfig)
worker.conf.BROKER_URL = configuration.get('celery', 'BROKER_URL')
worker.conf.CELERY_RESULT_BACKEND = configuration.get('celery', 'CELERY_RESULT_BACKEND')
