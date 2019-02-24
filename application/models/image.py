#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/24 20:12
"""
from application.extensions import db
from application.models.base import BaseModel


class Image(BaseModel):
    """用户上传图片"""
    __tablename__ = 'image'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), comment='上传的用户')
    default_show = db.Column(db.String(200), comment='默认上传显示的地址')
    raw = db.Column(db.Text)

