#!/usr/bin/env python
"""friends1
    cgi test
"""

import cgi

resthtml = '''Content-Type:text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for:<I>%s</I></H3>
Your name is:<B>%s</B><p>
You have <B>%s</B> friends.
</BODY></HTML>
'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print resthtml % (who, who, howmany)
