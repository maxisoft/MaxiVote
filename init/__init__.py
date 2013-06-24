#!/usr/bin/python
# -*- coding: UTF-8 -*-
import types
import os
import glob
from theglobals import *

class InitObj(object):
	"""Conteneur de fonctions"""
	def __init__(self):
		super(InitObj, self).__init__()
		self.allfct = []

	def addFct(self, fct):
		assert isinstance(fct, types.FunctionType)
		if fct in self.allfct:
			return
		setattr(self, fct.__name__, fct)
		self.allfct.append(fct)

	def __iadd__(self, fct):
		self.addFct(fct)
		return self
	
	def startInitScript(self):
		if not os.path.exists('./init'):
			return 0
		# else
		os.chdir('./init')
		for f in glob.glob("*.py"):
			if f.startswith("__"):
				continue
			execfile(f)
		os.chdir('../')
		
		return 1

	def __call__(self):
		"""Start all init script"""
		self.startInitScript()
		return self