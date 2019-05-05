#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/5 21:47
"""


def response(status, message, data):
    """
    基础返回方法封装
    :param status:
    :param message:
    :param data:
    :return:
    """
    return {'status': status, 'message': message, 'data': data}


def success_response(data):
    """
    成功返回
    :param data:
    :return:
    """
    return response(True, '操作成功', data=data)


def fail_response(message):
    """
    错误返回
    :param message:
    :return:
    """
    return response(False, message, None)
