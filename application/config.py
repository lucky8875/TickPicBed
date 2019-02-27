#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
配置文件
__author__= 'jiangyixin'
__time__ = 2019/2/22 21:20
"""
import os


# 项目根目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    pass


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@192.168.32.200:3306/tickpic'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """测试环境配置"""
    pass


class ProductionConfig(Config):
    """生成环境配置"""
    pass


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig
}
