# -*- coding: utf-8 -*-

from request_handler import request_get
import configuration as cf 

def get_products_info():
    req_url = cf.get('dashboard_service', 'SERVER_URL') + cf.get('dashboard_service', 'API_PRODUCT_INFO')
    return request_get(req_url=req_url, headers={'Authorization': 'Bearer 3A9A34CF-12CD-4A56-B18D-71D9FD3654BD'})


def get_prod_ver_error_collection(prod, version, page=1, pageSize=30):
    req_url = cf.get('dashboard_service', 'SERVER_URL') + (cf.get('dashboard_service', 'API_PROD_VER_ERRORCOL') %(prod))
    return request_get(
                req_url=req_url, 
                headers={'Authorization': 'Bearer 3A9A34CF-12CD-4A56-B18D-71D9FD3654BD'},
                version=version,
                pageSize=pageSize,
                page=page
    )


def get_prod_feature_dropbox_ids(prod, feature_id):
    req_url = cf.get('dashboard_service', 'SERVER_URL') + cf.get('dashboard_service', 'API_QUERY_DROPBOX_IDS')
    return request_get(
                req_url=req_url,
                headers={'Authorization': 'Bearer 3A9A34CF-12CD-4A56-B18D-71D9FD3654BD'},
                product=prod,
                errorfeature=feature_id
    )