#!/usr/bin/env python
'''PFAtest
    PFA application
'''
# import functions

from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showerror, showinfo, showwarning

# define constant

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

# define title
SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    '55\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU,
}

# define callback functions
critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
reguCB = lambda: showinfo('Info', 'Info Button Pressed!')

# define top
top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit,
       bg='red', fg='white').pack()

# define Buttontype by PFA
MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=reguCB, bg='white')

# define loop to create the billboard
for eachSign in SIGNS:
    signtype = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=1)' % (
        signtype.title(), eachSign,
        '.upper()' if signtype == CRIT else '.title()'
    )
    eval(cmd)

top.mainloop()
