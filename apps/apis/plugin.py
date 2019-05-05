#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/5 22:15
"""
from flask import Blueprint


plugin = Blueprint(__name__, 'plugin')


@plugin.route('/plugins')
def plugins():
    """
    获取插件列表
    :return:
    """
