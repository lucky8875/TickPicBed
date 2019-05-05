#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:28
"""
from flask import Flask
from apps.libs.plugin.plugin import manager
from apps.config import config
from apps.extensions import (
    db,
    migrate,
)


def create_app(env):
    """
    创建flask app实例
    :param env:
    :return:
    """
    if not env:
        env = 'default'
    cfg = config.get(env)
    app = Flask(__name__)
    configure_app(app, cfg)
    configure_extensions(app)
    register_blueprint(app)
    register_plugins(manager)
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
    migrate.init_app(app, db)
    dyconf.init_app(app)


def register_blueprint(app: Flask):
    """
    注册api资源
    :param app:
    :return:
    """
    from apps.apis import account
    from apps.apis import image
    app.register_blueprint(account, url_prefix='/v1/account')
    app.register_blueprint(image, url_prefix='/v1/image')


def register_plugins(manager):
    from apps.plugins.sm import SmPlugin
    manager.register_plugin('sm', SmPlugin)
