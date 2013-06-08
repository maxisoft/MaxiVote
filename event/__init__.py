#!/usr/bin/python
# -*- coding: UTF-8 -*-

from eventhook import EventHook, SetReturn, StopFire
from eventsdicts import EventsDict




#Global
EVENTS = EventsDict()

import functools


def eventOnFct(s):
	"""
	Decorator.
	call Event when a function is called
	"""

	assert (isinstance(s, str) and s != "")

	def mydecorator(func):
		@functools.wraps(func)
		def wrapper(*args, **keywargs):
			ret = func(*args, **keywargs)
			EVENTS[s](*args, **keywargs)
			return ret

		return wrapper

	return mydecorator
	