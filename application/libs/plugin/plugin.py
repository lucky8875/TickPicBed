#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/25 22:11
"""

import abc
import importlib


class PluginManager(object):
    """
    插件管理器
    """

    def __init__(self):
        """
        初始化时，先读取配置文件获取插件们所在的路径，
        然后扫描该路径将插件加载至插件管理器中
        """
        self._plugins = []
        self.load_plugins(['application.plugins.sm'])

    def load_plugins(self, plugin_modules):
        for plugin_module in plugin_modules:
            module = importlib.import_module(plugin_module)
            for plugin in dir(module):
                attr = getattr(module, plugin)
                if isinstance(attr, type) and BasePlugin in attr.__bases__:
                    if plugin not in self._plugins:
                        self.add_plugin(attr.plugin_name, attr)

    def add_plugin(self, plugin_name, cls):
        if plugin_name not in self._plugins:
            self._plugins.append({plugin_name: cls})


class BasePlugin(metaclass=abc.ABCMeta):
    """
    插件基类，所有插件必须实现此方法
    """

    @abc.abstractmethod
    def upload(self) -> str:
        """
        抽象上传方法
        :return: 可访问的图片的地址
        """
        pass


manager = PluginManager()
