#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/25 22:30
"""
import requests

from apps.libs.plugin.base_plugin import BasePlugin
from apps.libs.response import success_response, fail_response


class CcPlugin(BasePlugin):

    @staticmethod
    def upload(file) -> str:
        files = {
            'uploaded_file[]': file
        }
        response = requests.post('https://upload.cc/image_upload', files=files)
        result = response.json()
        data = result.get('data', {})
        if result.get('code') == 100:
            for url in result.get('success_image'):
                pass
        return fail_response(data.get('msg', ''))

    class Meta:
        plugin_plural_name = 'cc图床'
        plugin_name = 'cc'
