#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import defaultdict
import copy

from eventhook import EventHook

__all__ = ["EventsDict"]


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
		Allow to hook an existing event to do smthg before.
		"""
		tmp = copy.copy(self[key])  # copy the event (to save __handlers list )
		self[key].clearAll()
		self[key] += fct  # add new function
		self[key] += tmp  #  remember that EventHook instances are callable :)