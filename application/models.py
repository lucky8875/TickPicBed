#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/3/4 22:07
"""
from application.extensions import db
import datetime

from application.libs.model import ModelMixin


class BaseModel(db.Model):
    """基类"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='修改时间')


class Image(BaseModel, ModelMixin):
    """用户上传图片"""
    __tablename__ = 'image'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), comment='上传的用户')
    default_show = db.Column(db.String(200), comment='默认上传显示的地址')
    raw = db.Column(db.Text)


class User(BaseModel, ModelMixin):
    __tablename__ = 'user'

    nickname = db.Column(db.String(32), unique=True, comment='用户名')
    email = db.Column(db.String(50), unique=True, comment='邮箱')
    password = db.Column(db.String(32), nullable=True, comment='密码')
    secret_token = db.Column(db.String(32), nullable=True, comment='访问密匙')
    salt = db.Column(db.String(32), nullable=True, comment='密码盐')
