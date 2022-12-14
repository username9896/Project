from tkinter import *
from tkinter.ttk import Combobox
import random
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

screen = Tk()
screen.title("Health Monitoring System")
screen.geometry('600x600')
screen.configure(background="bisque")

def func():
    screen = Tk()
    screen.title("Student Data")
    screen.geometry('600x600')
    myvar = c1.get()
    if myvar.isdigit() == True:
        if len(str((myvar))) <= 10 and len(str((myvar))) > 9:
            ta = Label(screen, text='Displaying Student Data', font=('Arial', 25), fg='red', background="bisque")
            ta.place(x=120, y=0)
        else:
            tb = Label(screen, text='The entered Student ID is Invalid', font=('Arial', 24), background="bisque")
            tb.place(x=70, y=300)
    else:
        tb = Label(screen, text='The entered Student ID is Invalid', font=('Arial', 24), background="bisque")
        tb.place(x=70, y=300)


sc1 = StringVar('')
t1 = Label(screen, text='Health Monitoring System', font=('Arial', 25), fg='red', background="bisque")
t1.place(x=110, y=0)
t2 = Label(screen, text='Start Face Recognization:', font=('Arial', 14), background="bisque")
t2.place(x=70, y=90)
il = Button(screen, text='Start',font=('Arial', 14), fg='red', background="white")
il.place(x=310, y=85)
t3 = Label(screen, text='OR', font=('Arial', 14),  fg='red', background="bisque")
t3.place(x=260, y=155)
t4 = Label(screen, text='Enter Student ID: ', font=('Arial', 14),  fg='black', background="bisque")
t4.place(x=135, y=215)
c1 = Entry(screen, font=('Arial', 14), width=10)
c1.place(x=310, y=213)
b = Button(screen, text='OK', font=('Arial', 14), fg='red', background="white", command = func)
b.place(x=430, y=210)

screen.mainloop()
