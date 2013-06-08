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




class Plugin(object):
	__metaclass__ = ABCMeta
	pluginprior = 0
	def __init__(self, name=None, prior=None):
		self._pluginname = name
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
		self.dir = os.path.join(os.path.dirname(sys.argv[0]), 'plugin')
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
			if os.path.exists(os.path.join(self.dir,plugin, 'disable')) or os.path.exists(os.path.join(self.dir,plugin, 'disabled')):
				continue
			#else
			try:
				__import__(plugin)
			except ImportError, e:
				self.logger.exception("import error with folder : %s (no __init__.py ?)" , plugin)
			except Exception, e:
				self.logger.exception("can't import %s",plugin)
		
		# start plugins main method
		self.pluginsclasses = Plugin.AllRunnablePlugins()

		def sort_fct(l, r):
			return l.pluginprior - r.pluginprior

		self.pluginsclasses.sort(sort_fct)
		self.pluginsclasses = set(self.pluginsclasses)
		self.plugins = set([klass() for klass in self.pluginsclasses])
		for plugin in self.plugins:
			try:
				plugin.start()
			except Exception:
				self.logger.exception("Plugin : '%s' error during starting", plugin)
			else:  # ie sucess !
				EVENTS["PLUGIN_%s_START" % str(plugin.pluginname).upper()]()
				print "started `%s`" % plugin
		
			
	def __call__(self, *args):
		print """ === PLUGINS START ==="""
		ret = self.start(*args)
		print """ === PLUGINS STARTED ==="""
		return ret
	
	def __contains__(self, item):
		return item in self.plugins
			
		

PLUGINLIST = PluginsList()
