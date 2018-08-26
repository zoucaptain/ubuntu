#!/usr/bin/env python
"""urlopenAuth
    urllib2 application
"""

import urllib2

LOGIN = 'root'
PASSWORD = "123"
URL = 'http://localhost'


def handler_version(url):
    from urlparse import urlparse as up
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', up(url)[1], LOGIN, PASSWORD)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url


def request_version(url):
    from base64 import encodestring
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWORD))[:-1]
    req.add_header("Authorization", "Basic %s" % b64str)
    return req


for functype in ('handler', 'request'):
    print '*** Using %s' % functype.upper()
    url = eval('%s_version' % functype)(URL)
    f = urllib2.urlopen(url)
    print f.readline()
    f.close()
