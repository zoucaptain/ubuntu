#!/usr/bin/env python
"""friends2
    integrate static and dynamic page
"""

import cgi
from urllib import quote_plus
from string import capwords

header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/friends3.py'

errhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''


def showError(error_str):
    print header + errhtml % (error_str)


formhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for:<I>%s</I></H3>
<FORM ACTION="%s">
<B>Enter your name:</B>
<INPUT TYPE=hidden NAME=action VALUE=edit>
<INPUT TYPE=text NAME=person VALUE="%s" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>
'''

fradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'


def showForm(who, howmany):
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checkd = ''
        if str(i) == howmany:
            checkd = 'CHECKED'
        friends = friends + fradio % \
                  (str(i), checkd, str(i))
    print header + formhtml % (who, url, who, friends)


resthtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for:<I>%s</I></H3>
Your name is:<B>%s</B><p>
You have <B>%s</B> friends.
<p>Click <A HREF="%s">here</A> to edit your data again.
</BODY></HTML>
'''


def doResult(who, howmany):
    newurl = url + '?action=reedit&person=%s&howmany=%s' % \
             (quote_plus(who), howmany)
    print header + resthtml % (who, who, howmany, newurl)


def process():
    error = ''
    form = cgi.FieldStorage()

    if form.has_key('person'):
        who = capwords(form['person'].value)
    else:
        who = 'NEW USER'

    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        if form.has_key('action') and form['action'].value == 'edit':
            error = 'please select number of friends.'
        else:
            howmany = 0

    if not error:
        if form.has_key('action') and form['action'].value != 'reedit':
            doResult(who, howmany)
        else:
            showForm(who, howmany)
    else:
        showError(error)


if __name__ == '__main__':
    process()
