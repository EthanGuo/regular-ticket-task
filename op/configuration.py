# -*- coding: utf-8 -*-

import ConfigParser

cp = ConfigParser.ConfigParser()
cp.read('config/config.cfg')


def get(section, key):
    return cp.get(section, key)


def getint(section, key):
    return cp.getint(section, key) 