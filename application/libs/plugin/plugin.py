#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__= 'jiangyixin'
__time__ = 2019/2/25 22:11
"""
import abc


class BasePlugin(metaclass=abc.ABCMeta):
    """
    插件基类，所有插件必须实现此方法
    """

    @abc.abstractmethod
    def upload(self, file) -> str:
        """
        抽象上传方法
        :param file: 上传的文件对象
        :return: 可访问的图片的地址
        """
        pass

    @abc.abstractmethod
    def load_config(self) -> dict:
        """
        自定义加载插件配置
        :return: 插件配置键值对
        """
        pass


class PluginManager(object):
    """
    插件管理器
    """

    def __init__(self):
        """
        初始化时，先读取配置文件获取插件们所在的路径，
        然后扫描该路径将插件加载至插件管理器中
        """
        self._plugins = dict()

    def register_plugin(self, plugin_name, cls):
        if plugin_name not in self._plugins:
            self._plugins[plugin_name] = cls()

    def get_plugin(self, plugin_name) -> BasePlugin:
        """
        获取插件实例
        :param plugin_name:
        :return:
        """
        return  self._plugins.get(plugin_name, None)


manager = PluginManager()
