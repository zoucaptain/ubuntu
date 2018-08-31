#!/usr/bin/env python
"""friends2
    integrate static and dynamic page
"""

import cgi

header = 'Content-Type: text/html\n\n'

formhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for:<I>NEW USER</I></H3>
<FORM ACTION="/cgi-bin/friends2.py">
<B>Enter your name:</B>
<INPUT TYPE=hidden NAME=action VALUE=edit>
<INPUT TYPE=text NAME=person VALUE="NEW USER" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>
'''

fradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'


def showForm():
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checkd = ''
        if i == 0:
            checkd = 'CHECKED'
        friends = friends + fradio % \
                  (str(i), checkd, str(i))
    print header + formhtml % (friends)


resthtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for:<I>%s</I></H3>
Your name is:<B>%s</B><p>
You have <B>%s</B> friends.
</BODY></HTML>
'''


def doResult(who, howmany):
    print header + resthtml % (who, who, howmany)


def process():
    form = cgi.FieldStorage()
    if form.has_key('person'):
        who = form['person'].value
    else:
        who = 'NEW USER'
    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        howmany = 0
    if form.has_key('action'):
        doResult(who, howmany)
    else:
        showForm()


if __name__ == '__main__':
    process()
