#!/usr/bin/python
# -*- coding: UTF-8 -*-
import locale

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