#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import defaultdict
import copy

from eventhook import EventHook



def createDefaultEventHook():
	return EventHook()


class EventsDict(defaultdict):
	"""
	Use defaultDict in order to access/store events.
	"""

	def __init__(self, *args, **kwargs):
		super(EventsDict, self).__init__(createDefaultEventHook)
		self.update(*args, **kwargs)

	def __setitem__(self, key, val):
		ret = super(EventsDict, self).__setitem__(key, val)
		self[key].name = str(key)
		return ret


	def preHook(self, key, fct):
		"""
		Allow to hook an existing event to do smthg before calling this last.
		#TODO
		"""
		tmp = copy.copy(self[key]) #copy the event (to save __handlers list )
		self[key].clearAll() #clear all __handlers in curr 
		self[key] += fct # add new function
		self[key] += tmp #because tmp is a copy and is callable it work :)
		
		
		