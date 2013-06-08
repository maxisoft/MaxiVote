#!/usr/bin/python
# -*- coding: UTF-8 -*-

from theglobals import EVENTS, INIT_OBJ
from plugin import PLUGINLIST


if __name__ == '__main__':
	
	EVENTS["init"] += INIT_OBJ
	EVENTS["init"] += PLUGINLIST
	
	EVENTS["init"]()
	pass