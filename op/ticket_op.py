# -*- coding: utf-8 -*-

from bts import JiraHandler

OBJS = {'jira': JiraHandler}
BTS_OBJ = None


def init_bts_obj(bts_info):
    global BTS_OBJ
    if bts_info['type'] in OBJS.keys():
        BTS_OBJ = OBJS[bts_info['type']](bts_info)


def get_ticket_status(**kwargs):
    global BTS_OBJ
    if BTS_OBJ:
        code, action = BTS_OBJ.get_ticket_status(kwargs)
        return dict(code=code, data={'action': action}, msg='')
    else:
        return dict(code=1, data={}, msg='Please init bts object first.')


def reopen_ticket(**kwargs):
    global BTS_OBJ
    if BTS_OBJ:
        code, ret = BTS_OBJ.reopen_ticket(kwargs)
        return dict(code=code, data={}, msg=ret)
    else:
        return dict(code=1, data={}, msg='Please init bts object first.')


def add_comment(**kwargs):
    global BTS_OBJ
    if BTS_OBJ:
        code, ret = BTS_OBJ.add_comment(kwargs)
        return dict(code=code, data={}, msg=ret)
    else:
        return dict(code=1, data={}, msg='Please init bts object first.')


def submit_ticket(**kwargs):
    global BTS_OBJ
    if BTS_OBJ:
        code, ret = BTS_OBJ.create_ticket(kwargs)
        return dict(code=code, data=ret, msg='')
    else:
        return dict(code=1, data={}, msg='Please init bts object first.')


def get_proj_components(**kwargs):
    global BTS_OBJ
    if BTS_OBJ:
        code, ret = BTS_OBJ.get_proj_components(kwargs)
        return dict(code=code, data={'components': ret}, msg='')
    else:
        return dict(code=1, data={}, msg='Please init bts object first.')


def get_ticket_dropbox_ids(**kwargs):
    global BTS_OBJ
    if BTS_OBJ:
        code, ret = BTS_OBJ.get_ticket_dropbox_ids(kwargs)
        return dict(code=code, data={'dropbox_ids': ret}, msg='')
    else:
        return dict(code=1, data={}, msg='Please init bts object first.')