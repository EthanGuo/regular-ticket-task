# -*- coding: utf-8 -*-

from request_handler import request_post
from utils import get_config


def write_ticket_info(product, feature_id, ticket_id, url):
    req_url = get_config('dashboard_service', 'SERVER_URL') + (get_config('dashboard_service', 'API_TICKET_INFO_SAVE') %(product, feature_id))
    return request_post(
            req_url=req_url,
            headers={'Authorization': 'Bearer 3A9A34CF-12CD-4A56-B18D-71D9FD3654BD', 'Content-Type': 'application/json'},
            data={'ticket':ticket_id, 'url':url}
    )