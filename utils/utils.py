#!/usr/bin/python
# -*- coding: UTF-8 -*-
import locale
import zlib
import socket
from base64 import b64decode, b64encode
import hashlib

from Crypto.Cipher import AES


def to_unicode(x):
	"""Try to convert the input to utf-8."""

	# return empty string if input is None
	if x is None:
		return ''

	# if this is not a string, let's try converting it
	if not isinstance(x, basestring):
		x = str(x)

	# if this is a unicode string, encode it and return
	if isinstance(x, unicode):
		return x.encode('utf-8')

	# now try a bunch of likely encodings
	encoding = locale.getpreferredencoding()
	try:
		ret = x.decode(encoding).encode('utf-8')
	except UnicodeError:
		try:
			ret = x.decode('utf-8').encode('utf-8')
		except UnicodeError:
			try:
				ret = x.decode('latin-1').encode('utf-8')
			except UnicodeError:
				ret = x.decode('utf-8', 'replace').encode('utf-8', 'ignore')
	return ret


def inheritors(klass):
	subclasses = set()
	work = [klass]
	while work:
		parent = work.pop()
		for child in parent.__subclasses__():
			if child not in subclasses:
				subclasses.add(child)
				work.append(child)
	return subclasses


def get_computer_hash_name():
	return hashlib.sha224(socket.gethostname()).hexdigest()

def read_iv(file):
	ret = None
	with open(file, 'rb') as f:
		ret = "".join(f.readline())
	ret = hashlib.sha224(ret).hexdigest()[:16]
	return ret

def crypt(s, iv):
	def encipher(S):
		return AES.new(hashlib.sha224(iv).hexdigest()[:32], AES.MODE_CFB, iv).encrypt(S)

	s = encipher(b64encode(s))
	return b64encode(zlib.compress(s))


def decrypt(s, iv):
	def decipher(S):
		return AES.new(hashlib.sha224(iv).hexdigest()[:32], AES.MODE_CFB, iv).decrypt(S)

	return b64decode(decipher(zlib.decompress(b64decode(s))))
