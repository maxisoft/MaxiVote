#!/usr/bin/python
# -*- coding: UTF-8 -*-

from theglobals import EVENTS, INIT_OBJ, PLUGINLIST
from multiprocessing import freeze_support

if __name__ == '__main__':
	freeze_support()
	EVENTS["init"] += INIT_OBJ
	EVENTS["init"] += PLUGINLIST
	
	EVENTS["init"]()
	pass