from tkinter import *
from tkinter.ttk import Combobox
import random
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

screen = Tk()
screen.title("Password Generator")
screen.geometry('600x400')
screen.configure(background="bisque")

def func():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100,100,200,50)
    b.move(50,20)
    w.setWindowTitle("PyQt5")
    w.show()
    sys.exit(app.exec_())
    if __name__ == '__main__':
        window()


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
t4.place(x=145, y=215)
c1 = Entry(screen, font=('Arial', 14), width=10)
c1.place(x=310, y=213)

b = Button(screen, text='OK', font=('Arial', 14), fg='red', background="white")
b.place(x=340, y=260)

screen.mainloop()
