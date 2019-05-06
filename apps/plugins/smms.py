#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/25 22:30
"""
import requests

from apps.libs.plugin.base_plugin import BasePlugin
from apps.libs.response import success_response, fail_response


class SmPlugin(BasePlugin):

    @staticmethod
    def upload(file) -> str:
        data = {
            'ssl': True,
            'format': 'json'
        }
        files = {
            'smfile': file
        }
        response = requests.post('https://sm.ms/api/upload', data=data, files=files)
        result = response.json()
        data = result.get('data', {})
        if result.code == 'success':
            url = data.get('url', '')
            if not url:
                return fail_response('文件上传失败')
            return success_response(url)
        return fail_response(data.get('msg', ''))

    class Meta:
        plugin_plural_name = 'SMMS图床'
        plugin_name = 'smms'
