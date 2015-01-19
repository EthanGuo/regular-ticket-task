# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader


def renderTemplate(template, data):
    env = Environment(loader=FileSystemLoader('templates/ticket'))
    temp = env.get_template(template)
    return temp.render(data)


def check_request_data(data):
    if not data.get('type'):
        return False
    if not data.get('url'):
        return False
    if not data.get('username'):
        return False
    if not data.get('password'):
        return False
    return data