#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/4 22:09
"""
from flask import Blueprint

account = Blueprint(__name__, 'account')


@account.route('/create')
def account_create():
    """
    用户创建
    :return:
    """
