import importlib

from apps.libs.plugin.base_plugin import BasePlugin


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
        self.load_all_plugins()

    def load_all_plugins(self):
        """
        加载所有可用的插件
        :return:
        """
        plugins = importlib.import_module('apps.plugins')
        for item in dir(plugins):
            ins = getattr(plugins, item)
            if isinstance(ins, type) and issubclass(ins, BasePlugin):
                self._plugins.append({
                    'cls': ins,
                    'plugin_name': ins.Meta.plugin_name,
                    'plugin_plural_name': ins.Meta.plugin_plural_name
                })

    def get_all_plugins(self):
        return self._plugins

    def get_select_plugins(self, plugin_list=None):
        """
        获取用户选择的插件 默认全部选择
        :param plugin_list:
        :return:
        """
        if plugin_list is None:
            return self._plugins
        results = []
        for item in self._plugins:
            if item.get('plugin_name', '') in plugin_list:
                results.append(item)
        return results


manager = PluginManager()
