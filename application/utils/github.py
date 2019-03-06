#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/6 22:25
"""


def get_access_token(text):
    """
    获取access_token
    :param text:
    :return:
    """
    for item in text.split('&'):
        if 'access_token' in item:
            return item.split('=')[1]
    return ''
