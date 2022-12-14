from tkinter import *
from tkinter.ttk import Combobox
import random
import sys
from tkinter import messagebox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

screen = Tk()
screen.title("Health Monitoring System")
screen.geometry('600x600')
screen.configure(background="bisque")

def func():
    myvar = c1.get()
    if myvar.isdigit() == True:    
        if len(str((myvar))) <= 10 and len(str((myvar))) > 9:
            screen = Tk()
            screen.title("Student Data")
            screen.geometry('600x600')
            ta = Label(screen, text='Displaying Student Data', font=('Arial', 26), fg='red', background="bisque")
            ta.place(x=120, y=0)
            tq = Label(screen, text='Student Picture', font=('Arial', 26), fg='red')
            tq.place(x=160, y=200)
            tw = Label(screen, text='Student Name: ', font=('Arial', 20), fg='red')
            tw.place(x=50, y=300)
            te = Label(screen, text='Student Name', font=('Arial', 20), fg='red')
            te.place(x=260, y=300)
            tr = Label(screen, text='Student ID: ', font=('Arial', 20), fg='red')
            tr.place(x=50, y=340)
            tt = Label(screen, text='Student ID', font=('Arial', 20), fg='red')
            tt.place(x=260, y=340)
            ty = Label(screen, text='Guadian mail: ', font=('Arial', 20), fg='red')
            ty.place(x=50, y=380)
            tu = Label(screen, text='Guadian mail', font=('Arial', 20), fg='red')
            tu.place(x=260, y=380)
            ti = Label(screen, text='Start Checkup: ', font=('Arial', 20), fg='red')
            ti.place(x=50, y=420)
            il = Button(screen, text='Start',font=('Arial', 16), fg='red', background="white", command = start)
            il.place(x=260, y=420)
            ts = Label(screen, text='Previous Data: ', font=('Arial', 20), fg='red')
            ts.place(x=50, y=460)
            ig = Button(screen, text='See',font=('Arial', 16), fg='red', background="white", command = see)
            ig.place(x=260, y=460)
        elif len(str((myvar))) > 10 or len(str((myvar))) < 10:
            messagebox.showerror("Error","Entered ID is Invalid")
    elif myvar.isdigit() == False:
        messagebox.showerror("Error", "Entered ID is Invalid")


def start():
    screen = Tk()
    screen.title("Student Checkup")
    screen.geometry('600x600')
    tq = Label(screen, text='Sensor 1:', font=('Arial', 20), fg='red', background="bisque")
    tq.place(x=50, y=150)
    iq = Button(screen, text='start',font=('Arial', 16), fg='red', background="white")
    iq.place(x=200, y=150)
    tq = Label(screen, text='Sensor Data:', font=('Arial', 20), fg='red', background="bisque")
    tq.place(x=400, y=150)
    tw = Label(screen, text='Sensor 2: ', font=('Arial', 20), fg='red', background="bisque")
    tw.place(x=50, y=200)
    iw = Button(screen, text='Start',font=('Arial', 16), fg='red', background="white")
    iw.place(x=200, y=200)
    tq = Label(screen, text='Sensor Data:', font=('Arial', 20), fg='red', background="bisque")
    tq.place(x=400, y=200)
    te = Label(screen, text='Sensor 3:', font=('Arial', 20), fg='red', background="bisque")
    te.place(x=50, y=250)
    ie = Button(screen, text='Start',font=('Arial', 16), fg='red', background="white")
    ie.place(x=200, y=250)
    tq = Label(screen, text='Sensor Data:', font=('Arial', 20), fg='red', background="bisque")
    tq.place(x=400, y=250)
    tr = Label(screen, text='Sensor 4: ', font=('Arial', 20), fg='red', background="bisque")
    tr.place(x=50, y=300)
    ir = Button(screen, text='Start',font=('Arial', 16), fg='red', background="white")
    ir.place(x=200, y=300)
    

def see():
    screen = Tk()
    screen.title("Student Previous Data")
    screen.geometry('600x600')
    

sc1 = StringVar('')
t1 = Label(screen, text='Health Monitoring System', font=('Arial', 26), fg='red', background="bisque")
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

