#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:11
"""
from flask import Flask
from application.extensions import (
    db,
    alembic
)


def create_app(config):
    """
    创建flask app实例
    :param config:
    :return:
    """

    app = Flask(__name__)
    configure_app(app, config)
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
    alembic.init_app(app)
