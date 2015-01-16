# -*- coding: utf-8 -*-

import configuration as cf
from request_handler import request_post


def get_ticket_status(**kwargs):
    req_url = cf.get('ticket_service', 'SERVER_URL') + cf.get('ticket_service', 'API_TICKET_STATUS')
    return request_post(req_url, {'Content-Type': 'application/json'}, kwargs)


def reopen_ticket(**kwargs):
    req_url = cf.get('ticket_service', 'SERVER_URL') + cf.get('ticket_service', 'API_TICKET_REOPEN')
    return request_post(req_url, {'Content-Type': 'application/json'}, kwargs)


def add_comment(**kwargs):
    req_url = cf.get('ticket_service', 'SERVER_URL') + cf.get('ticket_service', 'API_TICKET_COMMENT')
    return request_post(req_url, {'Content-Type': 'application/json'}, kwargs)


def submit_ticket(**kwargs):
    req_url = cf.get('ticket_service', 'SERVER_URL') + cf.get('ticket_service', 'API_TICKET_CREATE')
    return request_post(req_url, {'Content-Type': 'application/json'}, kwargs)


def get_proj_components(**kwargs):
    req_url = cf.get('ticket_service', 'SERVER_URL') + cf.get('ticket_service', 'API_PROJ_COMPONENTS')
    return request_post(req_url, {'Content-Type': 'application/json'}, kwargs)