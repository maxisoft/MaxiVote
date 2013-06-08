#!/usr/bin/python
# -*- coding: UTF-8 -*-

import platform
import urllib2
import cookielib
import logging

logging.basicConfig(filename='MaxiVote.log', format='''
--------------------------
%(name)s @ %(asctime)s %(levelname)s:%(message)s
--------------------------
''', level=logging.DEBUG)

from lib.configobj import ConfigObj

CONFIG = ConfigObj("config.ini")

from init import INIT_OBJ
from event import EVENTS, eventOnFct
from event import SetReturn as SetReturn_Exception
from event import StopFire as StopFire_Exception
from utils.run_async import run_async

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