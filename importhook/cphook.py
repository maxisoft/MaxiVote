__author__ = 'maxisoft'


class CherryPyHook(object):
	name = None

	def __init__(self):
		self.name = self.name or self.__class__.__name__
