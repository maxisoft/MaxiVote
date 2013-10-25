#!/usr/bin/python
# -*- coding: UTF-8 -*-
from threading import Thread, Event
import time

from theglobals import EVENTS


class MyTimer(Thread):
	"""Call a function after a specified number of seconds. Repeat a specified number of times:

	Set repetitions to 0 to do this forever (until cancel is called).
	Usage:
	t = MyTimer(interval, repetitions, function, args=[], kwargs={})
	t.start()
	t.cancel() # stop the timer's action if it's still waiting
	"""
	# This timer is modeled after the original Timer class in the python threading package

	def __init__(self, interval, repetitions, function, event=None, args=[], kwargs={}):
		Thread.__init__(self)
		self.interval = interval
		self.repetitions = repetitions
		self.function = function
		self.args = args
		self.kwargs = kwargs
		self.finished = Event()
		self.event = event

	def cancel(self):
		"""Stop the timer if it hasn't finished yet"""
		self.finished.set()

	def run(self):
		if self.repetitions != 0:
			for i in range(0, self.repetitions):
				self.finished.wait(self.interval)
				if not self.finished.isSet():
					if(self.event):
						EVENTS[self.event]()
						
					self.function(*self.args, **self.kwargs)
		else:
			while not self.finished.isSet():
				self.finished.wait(self.interval)
				if not self.finished.isSet():
					self.function(*self.args, **self.kwargs)
		self.finished.set()
		
	def __call__(self):
		return self.start()
