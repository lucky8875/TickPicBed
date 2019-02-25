#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/25 22:30
"""
from application.utils.core.plugin import BasePlugin


class SmPlugin(BasePlugin):
    def upload(self) -> str:
        return 'sm'
