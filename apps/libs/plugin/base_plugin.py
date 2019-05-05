#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/25 22:11
"""


class BasePlugin(object):
    """
    插件基类，所有插件必须实现此方法
    """

    @staticmethod
    def upload(file) -> str:
        """
        抽象上传方法
        :param file: 上传的文件对象
        :return: 可访问的图片的地址
        """
        raise Exception("必须实现插件上传方法")

