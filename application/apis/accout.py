#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/4 22:09
"""
import requests
from flask import Blueprint, request, abort, current_app, url_for

from application.utils.github import get_access_token

account = Blueprint(__name__, 'account')


@account.route('/create', methods=['POST'])
def account_create():
    """
    用户创建
    :return:
    """


@account.route('/oauth')
def account_oauth():
    """
    oauth 注册
    :return:
    """
    code = request.args.get('code')
    if not code:
        abort(500)
    config = current_app.config
    url = config.get('GITHUB_TOKEN_ACCESS_URL')
    params = {
        'client_id': config.get('GITHUB_CLIENT_ID'),
        'client_secret': config.get('GITHUB_CLIENT_SECRET'),
        'code': code,
    }
    res = requests.post(url=url, data=params)
    token = get_access_token(res.text)



@account.route('/demo')
def demo():
    return 's'
