#!/usr/bin/python
# -*- coding: UTF-8 -*-

import platform
import urllib2
import cookielib
import logging
import sys
import os

VERSION = int(1)

INSTALL_DIR = os.path.dirname(sys.argv[0])
PLUGIN_DIR = os.path.join(INSTALL_DIR, 'plugin')
LOG_DIR = os.path.join(INSTALL_DIR, 'log')
INIT_DIR = os.path.join(INSTALL_DIR, 'init')
#folder creation
if not os.path.isdir(LOG_DIR):
	os.mkdir(LOG_DIR)

if not os.path.isdir(INIT_DIR):
	os.mkdir(INIT_DIR)
KEY_PRIVATE_FILE = os.path.join(INSTALL_DIR, 'key.private')

logging.basicConfig(filename=os.path.join(LOG_DIR, 'MaxiVote.log'), format='''
--------------------------
%(name)s @ %(asctime)s %(levelname)s:%(message)s
--------------------------
''', level=logging.DEBUG)

from lib.configobj import ConfigObj
CONFIG = ConfigObj("config.ini")
INIT_OBJ = None
import init
INIT_OBJ = init.InitObj()
def registerInitFct(fct):
	"""
	Decorator.
	Permet de sauvegarder la fonction dans l'init object.
	"""
	INIT_OBJ.addFct(fct)
	return fct
from event import EVENTS, eventOnFct
from event import SetReturn as SetReturn_Exception
from event import StopFire as StopFire_Exception
from utils.run_async import run_async
PLUGINLIST = None
import plugin
PLUGINLIST = plugin.PluginsList()

COMPUTER_NAME = platform.node() or "unknow" #computer name (string). set to unknow if can't get it.
LOGGING = logging.getLogger("root") #super logger obj. For internal use

HTTP_PROXY = unicode(
	CONFIG['http_proxy']) if 'http_proxy' in CONFIG else None #proxy https string (like '127.0.0.1:8080')
HTTPS_PROXY = HTTP_PROXY = unicode(
	CONFIG['https_proxy']) if 'https_proxy' in CONFIG else None #proxy https string (like '127.0.0.1:8080')

PROXY_SUPPORT = urllib2.ProxyHandler({"http": HTTP_PROXY, "https": HTTPS_PROXY}) if (
HTTP_PROXY or HTTPS_PROXY) else None #proxy handler for urllib. set to None if not using proxy

URL_OPENER = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()), PROXY_SUPPORT) if PROXY_SUPPORT \
	else urllib2.build_opener(
	urllib2.HTTPCookieProcessor(cookielib.CookieJar())) #default URL opener (a urllib2 object). Use proxy if any .


import utils.utils