#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/25 22:19
"""
from application.config import base_path
import fnmatch
import os


def get_plugin_list(path):
    """
    获取所有插件的路径
    :param path:
    :return:
    """
    paths = []
    for f_name in os.listdir(os.path.join(base_path, *path.split('.'))):
        if fnmatch.fnmatch(f_name, '*.py') and f_name != '__init__.py':
            paths.append(f'{path}.{f_name[0:-3]}')
    return paths


if __name__ == '__main__':
    print(get_plugin_list('application.plugins'))
    pass