
# -*- coding: utf-8 -*-

from worker import worker
from op import ticket_worker


@worker.task(ignore_result=True)
def job_ticket_task():
    ticket_worker()