#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Flask统一初始化
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:30
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
