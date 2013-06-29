#!/usr/bin/python
# -*- coding: UTF-8 -*-

from multiprocessing import freeze_support
import os
import sys

from Crypto import Random

from theglobals import EVENTS, INIT_OBJ, PLUGINLIST, INSTALL_DIR, KEY_PRIVATE_FILE

from utils.singleinstance import singleinstance

if __name__ == '__main__':
	os.chdir(INSTALL_DIR)
	# do this at beginnig of your application
	myapp = singleinstance()

	# check is another instance of same program running
	if myapp.aleradyrunning():
		print "Another instance of this program is already running"
		os._exit(9)
	#key create
	if not os.path.isfile(KEY_PRIVATE_FILE):
		with open(KEY_PRIVATE_FILE, 'wb') as f:
			f.write(Random.get_random_bytes(32 << 8))
	sys.path.append(INSTALL_DIR)

	freeze_support()
	EVENTS["init"] += INIT_OBJ
	EVENTS["init"] += PLUGINLIST

	EVENTS["init"]()