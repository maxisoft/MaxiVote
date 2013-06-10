#!/usr/bin/python
# -*- coding: UTF-8 -*-
from theglobals import *
import os
import sys
import logging

from abc import ABCMeta, abstractmethod
from threading import Thread
from multiprocessing import Process
from utils.utils import inheritors


class LoggerFix(object):
	"""
	Allow "pickling" object with logger property.
	"""
	_logger = None

	def __init__(self, format="%(asctime)s %(filename)s, %(lineno)d, %(funcName)s: %(message)s"):
		self.__formatLogger = format
		self._logger = self.CreateLogger()

	@property
	def logger(self):
		"""I'm the 'x' property."""
		return self._logger or self.CreateLogger()

	@logger.deleter
	def logger(self):
		del self._logger

	def CreateLogger(self):
		self._logger = logging.Logger(self.__class__.__name__)
		try:
			self.logger.handlers[0].stream.close()
			self.logger.removeHandler(self.logger.handlers[0])
		except:
			pass
		file_handler = logging.FileHandler(os.path.join(LOG_DIR, self.__class__.__name__+'.log'))
		file_handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter(self.__formatLogger)
		file_handler.setFormatter(formatter)
		self.logger.addHandler(file_handler)
		return self.logger

	def __getstate__(self):
		d = dict(self.__dict__)
		del d['_logger']
		return d

	def __setstate__(self, d):
		self.__dict__.update(d)

class Plugin(LoggerFix):
	__metaclass__ = ABCMeta
	pluginprior = 0

	def __init__(self, name=None, prior=None):
		super(Plugin,self).__init__()
		self._pluginname = name or self.__class__.__name__
		if prior is not None:
			self.pluginprior=prior

	@property
	def pluginname(self):
		"""Get plugin Name"""
		return self._pluginname

	@abstractmethod
	def run(self):
		pass

	@staticmethod
	def isRunnable(pluginClasse):
		if "__abstractmethods__" in pluginClasse.__dict__ and "run" in pluginClasse.__dict__["__abstractmethods__"]:
			return False
		return True

	@staticmethod
	def AllRunnablePlugins():
		return filter(Plugin.isRunnable, inheritors(Plugin))

	def __cmp__(self, other):
		return self.pluginprior - other.pluginprior

	def __str__(self):
		return '<Plugin : "%s">' % self.pluginname



class PluginThread(Plugin, Thread):
	__metaclass__ = ABCMeta

	def __init__(self, name=None):
		super(PluginThread, self).__init__(name=name)
		Thread.__init__(self)
		self.setName(name)

	@abstractmethod
	def run(self):
		return NotImplemented

class RequieredPlugin(PluginThread):

	pluginprior = sys.maxint

	def __init__(self, name=None, tiemoutjoin=100):
		self.tiemoutjoin = tiemoutjoin
		super(RequieredPlugin, self).__init__(name)

	def start(self):
		ret = super(RequieredPlugin, self).start()
		self.join(self.tiemoutjoin)  # wait
		if self.is_alive():
			try:
				self._Thread__stop()
			except:
				pass
		return ret

	@abstractmethod
	def run(self):
		return NotImplemented


class PluginProcess(Plugin, Process):
	__metaclass__ = ABCMeta

	def __init__(self, name=None):
		super(PluginProcess, self).__init__(name=name)
		Process.__init__(self)
		self._name = name

	@abstractmethod
	def run(self):
		return NotImplemented


class PluginsList:
	def __init__(self):
		self.plugins = set()
		self.pluginsclasses = set()
		self.dir = PLUGIN_DIR
		if not os.path.isdir(self.dir):
			os.mkdir(self.dir)
		self.subdir = [name for name in os.listdir(self.dir) if os.path.isdir(os.path.join(self.dir, name))]
		sys.path.append(self.dir) # => easy import
		self.logger = logging.getLogger("plugin loader")
		
	@eventOnFct("ALL_PLUGINS_STARTED")
	def start(self, *args):
		# list all plugin
		for plugin in self.subdir:
			#check disabled
			if os.path.exists(os.path.join(self.dir, plugin, 'disable')) or os.path.exists(os.path.join(self.dir, plugin, 'disabled')):
				continue
			#else
			try:
				__import__(plugin)
			except ImportError, e:
				self.logger.exception("import error with folder : %s (no __init__.py ?)", plugin)
			except Exception, e:
				self.logger.exception("can't import %s", plugin)
		
		# start plugins
		self.pluginsclasses = Plugin.AllRunnablePlugins()

		def sort_fct(l, r):
			"""
			Sort plugin using prior attribute. decreasing.
			"""
			return -(r.pluginprior - l.pluginprior)

		self.pluginsclasses.sort(sort_fct)  # sort plugin
		self.pluginsclasses = set(self.pluginsclasses)  # convert to a set
		self.plugins = set([klass() for klass in self.pluginsclasses])  # instantiate every class
		print(self.plugins)
		for plugin in self.plugins:
			try:
				plugin.start()  # start plugin
			except Exception:
				self.logger.exception("%s error during starting", plugin)
			else:  # ie success !
				EVENTS["PLUGIN_%s_START" % str(plugin.pluginname).upper()]()  # Call Event
				print "started %s" % plugin

	def __call__(self, *args):
		print """ === PLUGINS START ==="""
		ret = self.start(*args)
		print """ === PLUGINS STARTED ==="""
		return ret
	
	def __contains__(self, item):
		return (item in self.plugins) or (item in self.pluginsclasses)