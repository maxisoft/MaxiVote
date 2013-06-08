#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 7 f�vr. 2013

@author: i5
'''

from initobject import InitObj


# GLOBAL
INIT_OBJ = InitObj()

def registerInitFct(fct):
	"""
	Decorator.
	Permet de sauvegarder la fonction dans l'init object.
	"""
	INIT_OBJ.addFct(fct)
	return fct
