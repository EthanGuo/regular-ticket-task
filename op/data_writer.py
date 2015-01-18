# -*- coding: utf-8 -*-

from request_handler import request_post
import configuration as cf 

def write_ticket_info(product, feature_id, ticket_id, url):
    req_url = cf.get('dashboard_service', 'SERVER_URL') + (cf.get('dashboard_service', 'API_TICKET_INFO_SAVE') %(product, feature_id))
    return request_post(
            req_url=req_url,
            headers={'Authorization': 'Bearer 3A9A34CF-12CD-4A56-B18D-71D9FD3654BD', 'Content-Type': 'application/json'},
            data={'ticket':ticket_id, 'url':url}
    )