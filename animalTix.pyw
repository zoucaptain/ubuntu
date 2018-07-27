#!/usr/bin/env python
'''animalTix
    animal GUI by Tix
'''
from Tkinter import Label, Button, END
from Tix import Tk, Control, ComboBox

# top
top = Tk()
top.tk.eval('package require Tix')

# label
lb = Label(top, text='in pairs')
lb.pack()
# control
ct = Control(top, label='Number:', integer=True, max=12, min=2, value=2, step=2)
ct.label.config(font='Helvetica -14 bold')
ct.pack()
# combobox
cb = ComboBox(top, label='Type:', editable=True)
for animal in ('dog', 'duck', 'hamster', 'cat'):
    cb.insert(END, animal)
cb.pack()
# button
qb = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()
