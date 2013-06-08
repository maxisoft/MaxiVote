__author__ = 'i5'

from plugin import *

class TestPlugin(PluginThread):

	pluginprior = 0

	def __init__(self):
		super(TestPlugin, self).__init__(name="Test")

	def run(self):
		import time
		while 1:
			print "it work"
			time.sleep(5)