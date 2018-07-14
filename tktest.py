#!/usr/bin/env python
'''tkinter test
    make a window
'''
from Tkinter import *


# adjust font big or small
def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())


# define top and area
top = Tk()
top.geometry('250x150')
# define label
label = Label(top, text='Hello world!',
              font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)
# define scale
scale = Scale(top, from_=10, to=40,
              orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)
# define Button for 'quit'
quit = Button(top, text='QUIT',
              command=top.quit, activeforeground='white',
              activebackground='red')
quit.pack()
# mainloop
mainloop()
