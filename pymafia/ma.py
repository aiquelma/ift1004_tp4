from tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

f1 = Frame(master)
f1.grid(column=1, row=1)
f2 = Frame(master)
f2.grid(column=1, row=2)
f1['highlightthickness'] = 1
f1['highlightbackground'] = 'black'
f2['highlightthickness'] = 1
f2['highlightbackground'] = 'black'
l = Label(f2, text="ic")
l.pack()
w = OptionMenu(f1, variable, "one", "two", "three")
w.pack()

mainloop()