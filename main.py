#!/usr/bin/python3
# By HookSander

from math import *
from tkinter import *

root = Tk()
root.geometry("500x700")
root.config(background='black')
root.title("Calculator")


title = Label(root, text='HookSAnder Calculator', font=('Arial', 10), bg='black', fg='white')
#title.place(x=190, y=10)
title.grid(row=0, column=0)

screen = Text(root, font=('Arial', 20), bg='white', height=1, width=30)
#screen.place(x=25, y=50)
screen.grid(row=1, column=0)

button7 = Button(root, text='7', font=('Arial', 20))
button7.grid(row=2, column=1)



root.mainloop()