#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/4 22:10
"""
from flask import Blueprint, request, jsonify
from apps.libs.plugin.plugin_manage import manager


image = Blueprint(__name__, 'image')


@image.route('/upload', methods=['POST'])
def upload():
    plugin = manager.get_plugin()
    if plugin is None:
        return
    result = plugin.upload(file=request.files.get('file'))
    return jsonify(result)
