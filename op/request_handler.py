# -*- coding: utf-8 -*-

import requests
import json


def request_post(req_url, headers, data):
    try:
        res = requests.post(url=req_url, headers=headers, data=json.dumps(data))
        if res.status_code == 200:
            return res.json()
        else:
            print "status_code: %d, reason: %s" %(res.status_code, res.reason)
            return {'code': 1, 'msg': 'request failed', 'data':{}}
    except Exception, e:
        print "Exception"
        return {'code': 1, 'msg': 'request failed', 'data':{}}


def request_get(req_url, headers, **kwargs):
    try:
        res = requests.get(url=req_url, headers=headers, params=kwargs)
        if res.status_code == 200:
            return res.json()
        else:
            return None
    except Exception, e:
        print e
        return None
