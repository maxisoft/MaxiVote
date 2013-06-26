#!/usr/bin/python
# -*- coding: UTF-8 -*-

from theglobals import EVENTS, INIT_OBJ, PLUGINLIST, LOG_DIR, INSTALL_DIR, KEY_PRIVATE_FILE
from multiprocessing import freeze_support
import os
from Crypto import Random
import sys
if __name__ == '__main__':
	#key create
	if not os.path.isfile(KEY_PRIVATE_FILE):
		with open(KEY_PRIVATE_FILE, 'wb') as f:
			f.write(Random.get_random_bytes(32 << 8))
	sys.path.append(INSTALL_DIR)
	import importhook
	freeze_support()
	EVENTS["init"] += INIT_OBJ
	EVENTS["init"] += PLUGINLIST

	EVENTS["init"]()