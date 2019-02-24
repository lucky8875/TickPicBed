#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/24 19:34
"""
from application.extensions import db
from application.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    nickname = db.Column(db.String(32), unique=True, comment='用户名')
    email = db.Column(db.String(50), unique=True, nullable=False, comment='邮箱')
    password = db.Column(db.String(32), nullable=False, comment='密码')
    secret_token = db.Column(db.String(32), nullable=False, comment='访问密匙')
    salt = db.Column(db.String(32), nullable=False, comment='密码盐')

