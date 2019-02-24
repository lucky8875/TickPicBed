#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:19
"""
import os
from flask_script import Manager
from application.app import create_app
from application.config import config

environment = os.getenv('DEVELOPMENT', 'default')
manage = create_app(config.get(environment))


