# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader


def renderTemplate(template, data):
    env = Environment(loader=FileSystemLoader('templates/ticket'))
    temp = env.get_template(template)
    return temp.render(data)