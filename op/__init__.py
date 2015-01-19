# -*- coding: utf-8 -*-

from db_op import *
from ticket_op import *
from utils import renderTemplate, get_config


# tool funcs

def valide_bts_info(bts_info):
    if not bts_info:
        return None
    for key in ['type', 'username', 'password', 'url', 'project', 'threshold', 'ver_control']:
        if key not in bts_info.keys() or not bts_info[key]:
            return None
    return bts_info


def get_target_versions(prod_info, bts_info):
    ver_control = bts_info.get('ver_control')
    ret = {}
    for ver_type in ver_control.keys():
        versions = prod_info.get('versions', {})
        if versions.get(ver_type):
            ret[ver_type] = [] if ver_control[ver_type] == 0 else versions[ver_type][-ver_control[ver_type]:]
        else:
            ret[ver_type] = []
    return ret


def get_dropbox_ids(product, feature_id):
    ret = get_prod_feature_dropbox_ids(product, feature_id)
    dropbox_ids = []
    if ret:
        for item in ret.get('data'):
            if item.get('_id'):
                dropbox_ids.append(item['_id'])
    return dropbox_ids


def append_ids(ticket_id, version, bts_info, product, ef, template_name):
    last_ids = get_dropbox_ids(product, ef.get('id'))
    org_ids = get_ticket_dropbox_ids(
                type=bts_info.get('type'),
                url=bts_info.get('url'),
                username=bts_info.get('username'),
                password=bts_info.get('password'),
                ticket_url=get_config('dashboard_service', 'API_QUERY_DROPBOX_DATA'),
                ticket_id=ticket_id)['data'].get('dropbox_ids', [])
    dropbox_ids = set(last_ids) - set(org_ids)
    if template_name == 'comment_append_ids.jinja2' and not dropbox_ids:
        return
    ret = add_comment(
            type=bts_info.get('type'),
            url=bts_info.get('url'),
            username=bts_info.get('username'),
            password=bts_info.get('password'),
            ticket_id=ticket_id,
            comment=renderTemplate(template_name, {
                'version': version,
                'url': get_config('dashboard_service', 'SERVER_URL') + get_config('dashboard_service', 'API_QUERY_DROPBOX_DATA'),
                'dropbox_ids': dropbox_ids})
    )


def detect_component(bts_info, ef):
    issue_owner, comp = ef.get('features', {}).get('issue_owner'), None
    if issue_owner:
        for k, v in bts_info.get('components', {}).iteritems():
            if issue_owner in v:
                comp = k
                break
    if not comp: 
        comp = 'Triage'
    return comp


# action response

def ticket_submit(product, version, ver_type, bts_info, ef):
    ret = submit_ticket(
            type=bts_info.get('type'),
            url=bts_info.get('url'),
            username=bts_info.get('username'),
            password=bts_info.get('password'),
            proj=bts_info.get('project'),
            comp=detect_component(bts_info, ef),
            sys_ver=version,
            summary=renderTemplate('ticket_summary.jinja2', {'product': product, 'ef': ef}),
            description=renderTemplate('ticket_description.jinja2', {
                'ef': ef, 
                'url': get_config('dashboard_service', 'SERVER_URL') + get_config('dashboard_service', 'API_QUERY_DROPBOX_DATA'),
                'dropbox_ids': get_dropbox_ids(product, ef.get('id'))})
    )
    if ret.get('code') == 0:
        ret = write_ticket_info(
                product=product,
                feature_id=ef.get('id'),
                ticket_id=ret.get('data', {}).get('ticket_id'),
                url=ret.get('data', {}).get('url'))
        # ensure this action or...


def ticket_reopen(ticket_id, version, bts_info, product, ef):
    ret = reopen_ticket(
            type=bts_info.get('type'),
            url=bts_info.get('url'),
            username=bts_info.get('username'),
            password=bts_info.get('password'),
            ticket_id=ticket_id)
    if ret.get('code') == 0:
        append_ids(ticket_id, version, bts_info, product, ef, 'comment_reopen.jinja2')


def ticket_no_fix_version(ticket_id, version, bts_info, product, ef):
    ret = add_comment(
            type=bts_info.get('type'),
            url=bts_info.get('url'),
            username=bts_info.get('username'),
            password=bts_info.get('password'),
            ticket_id=ticket_id,
            comment=renderTemplate('comment_no_fix_version.jinja2', {})
        )


def ticket_append_id(ticket_id, version, bts_info, product, ef):
    append_ids(ticket_id, version, bts_info, product, ef, 'comment_append_ids.jinja2')


def ticket_idle(ticket_id, version, bts_info, product, ef):
    pass


# main logic

ACTION_RESPONSE = {
    'submit_ticket': ticket_submit,
    'reopen': ticket_reopen,
    'no-fix-version': ticket_no_fix_version,
    'append-dropbox-id': ticket_append_id,
    'idle': ticket_idle
}

def go_through_efs(data, product, version, ver_type, bts_info):
    if data:
        threshold = bts_info.get('threshold')
        for ef in data:
            if ef.get('tag') in threshold.keys() and ef.get('count') >= threshold[ef.get('tag')]:
                if ef.get('tickets'):
                    for ticket in ef.get('tickets'):
                        if ticket.get('product') == product:
                            ret = get_ticket_status(
                                    type=bts_info.get('type'),
                                    url=bts_info.get('url'),
                                    username=bts_info.get('username'),
                                    password=bts_info.get('password'),
                                    ticket_id=ticket.get('id'),
                                    sys_ver=version
                            )
                            if ret.get('code') == 0:
                                print "Ticket: %s: %s" %(ticket.get('id'), ret['data'].get('action'))
                                ACTION_RESPONSE[ret['data'].get('action')](ticket.get('id'), version, bts_info, product, ef)
                            break
                    else:
                        ACTION_RESPONSE['submit_ticket'](product, version, ver_type, bts_info, ef)
                else:
                    ACTION_RESPONSE['submit_ticket'](product, version, ver_type, bts_info, ef)


def handle_prod_ver(product, version, ver_type, bts_info):
    print "Analyze: %s:%s(%s)" %(product, version, ver_type)
    version = '20150115.0137'
    ec = get_prod_ver_error_collection(product, version)
    if ec:
        go_through_efs(ec.get('data'), product, version, ver_type, bts_info)
        if ec.get('pages') != 1:
            for i in range(2, ec['pages'] + 1):
                ec = get_prod_ver_error_collection(product, version, i)
                if ec:
                    go_through_efs(ec.get('data'), product, version, ver_type, bts_info)


def ticket_worker():
    products_info = get_products_info()
    if products_info:
        for prod_info in products_info:
            product, bts_info = prod_info.get('_id'), valide_bts_info(prod_info.get('bts'))
            if not bts_info or not product:
                print "Error: %s: bts info missing" %(product)
                continue
            target_versions = get_target_versions(prod_info, bts_info)
            for ver_type in target_versions.keys():
                for version in target_versions[ver_type]:
                    handle_prod_ver(product, version, ver_type, bts_info)