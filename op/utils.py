# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import ConfigParser


cp = ConfigParser.ConfigParser()
cp.read('config/config.cfg')


def get_config(section, key):
    return cp.get(section, key)


def get_config_int(section, key):
    return cp.getint(section, key)


def renderTemplate(template, data):
    env = Environment(loader=FileSystemLoader('templates/ticket'))
    temp = env.get_template(template)
    return temp.render(data)