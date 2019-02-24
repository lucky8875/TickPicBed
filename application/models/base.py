#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/24 19:35
"""
from application.extensions import db
import datetime


class BaseModel(object):
    """基类"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='修改时间')

