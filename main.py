#!/usr/bin/python3
# By HookSander

from math import *
from tkinter import *

root = Tk()
root.geometry("500x700")
root.config(background='black')
root.title("Calculator")


title = Label(root, text='HookSAnder Calculator', font=('Arial', 10), bg='black', fg='white')
title.place(x=190, y=10)

screen = Text(root, font=('Arial', 20), bg='white', height=1, width=30)
screen.place(x=25, y=50)

button7 = Button(root, text='7', font=('Arial', 20), width=5)
button7.place(x=25, y=150)

button8 = Button(root, text='8', font=('Arial', 20), width=5)
button8.place(x=200, y=150)

button9 = Button(root, text='9', font=('Arial', 20), width=5)
button9.place(x=375, y=150)

button4 = Button(root, text='4', font=('Arial', 20), width=5)
button4.place(x=25, y=250)

button5 = Button(root, text='5', font=('Arial', 20), width=5)
button5.place(x=200, y=250)

button6 = Button(root, text='6', font=('Arial', 20), width=5)
button6.place(x=375, y=250)

button1 = Button(root, text='1', font=('Arial', 20), width=5)
button1.place(x=25, y=350)

button2 = Button(root, text='2', font=('Arial', 20), width=5)
button2.place(x=200, y=350)

button3 = Button(root, text='2', font=('Arial', 20), width=5)
button3.place(x=375, y=350)


root.mainloop()