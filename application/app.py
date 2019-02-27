#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:11
"""
from flask import Flask
from application.config import config
from application.extensions import (
    db,
)


def create_app(env):
    """
    创建flask app实例
    :param config:
    :return:
    """
    if not env:
        env = 'default'
    cfg = config.get(env)
    app = Flask(__name__)
    configure_app(app, cfg)
    configure_extensions(app)

    return app


def configure_app(app, config):
    """
    注册配置
    :param app:
    :param config:
    :return:
    """
    app.config.from_object(config)


def configure_extensions(app):
    """
    注册插件
    :param app:
    :return:
    """
    db.init_app(app)
