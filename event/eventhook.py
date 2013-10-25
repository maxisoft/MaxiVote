#!/usr/bin/python
# -*- coding: UTF-8 -*-
from time import sleep
import logging



class StopFire(Exception):
	"""
	raise this exception in order to stop next handlers during a event fire (EventHook.fire())
	"""
	pass


class SetReturn(Exception):
	""" raise this exception in order to set the return value"""
	def __init__(self, arg):
		super(SetReturn, self).__init__()
		self.arg = arg


class EventHook(object):
	def __init__(self, name="", delay=0):
		self.__handlers = list()
		self.name = str(name)
		self.count = 0
		self.delay = delay

	def __iadd__(self, handler):
		self.__handlers.append(handler)
		return self

	def __isub__(self, handler):
		self.__handlers.remove(handler)
		return self

	def fire(self, *args, **keywargs):
		return_val = None
		self.count += 1
		if self.delay:
			sleep(self.delay)

		for handler in self.__handlers:
			try:
				handler(*args, **keywargs)
			except SetReturn, e:
				return_val = e.arg
			except StopFire:
				break
			except Exception:
				logger_name = self.name.upper() + '_EVENT' if self.name else 'UNNAMED_EVENT'
				logger = logging.getLogger(logger_name)
				logger.exception("")

		return return_val

	def clearObjectHandlers(self, inObject):
		for theHandler in self.__handlers:
			if theHandler.im_self == inObject:
				self -= theHandler

	def clearAll(self):
		self.count = 0
		del self.__handlers[:]  # del content

	def __call__(self, *args, **keywargs):
		return self.fire(*args, **keywargs)

	def __len__(self):
		return len(self.__handlers)

	def __str__(self):
		return self.name
