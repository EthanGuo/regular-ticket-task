# -*- coding: utf-8 -*-

from bts import JiraHandler
from utils import check_request_data


OBJS = {'jira': JiraHandler}


def get_ticket_status(**kwargs):
    data = check_request_data(kwargs)
    if data and data['type'] in OBJS.keys():
        code, action = OBJS[data['type']](data).get_ticket_status(data)
        return dict(code=code, data={'action': action}, msg='')
    else:
        return dict(code=1, data={}, msg='required fields missing or illegal')


def reopen_ticket(**kwargs):
    data = check_request_data(kwargs)
    if data and data['type'] in OBJS.keys():
        code, ret = OBJS[data['type']](data).reopen_ticket(data)
        return dict(code=code, data={}, msg=ret)
    else:
        return dict(code=1, data={}, msg='required fields missing or illegal')


def add_comment(**kwargs):
    data = check_request_data(kwargs)
    if data and data['type'] in OBJS.keys():
        code, ret = OBJS[data['type']](data).add_comment(data)
        return dict(code=code, data={}, msg=ret)
    else:
        return dict(code=1, data={}, msg='required fields missing or illegal')


def submit_ticket(**kwargs):
    data = check_request_data(kwargs)
    if data and data['type'] in OBJS.keys():
        code, ret = OBJS[data['type']](data).create_ticket(data)
        return dict(code=code, data=ret, msg='')
    else:
        return dict(code=1, data={}, msg='required fields missing or illegal')


def get_proj_components(**kwargs):
    data = check_request_data(kwargs)
    if data and data['type'] in OBJS.keys():
        code, ret = OBJS[data['type']](data).get_proj_components(data)
        return dict(code=code, data={'components': ret}, msg='')
    else:
        return dict(code=1, data={}, msg='required fields missing or illegal')