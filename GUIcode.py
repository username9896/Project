#Libraries
import tkinter
from tkinter import *
from tkinter.ttk import Combobox
import random
import sys
from tkinter import messagebox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageTk
import time
import pymysql
from datetime import datetime
import os

#conencting to database
conn = pymysql.connect(host='localhost', user='localuser1', password='rootuser', database='sensordb')
cursor = conn.cursor()

screen = Tk()
screen.title("Health Monitoring System")
screen.geometry('600x600')
screen.configure(background="bisque")


def ExistingStudent():
    myvar = c1.get()
    if myvar.isdigit() == True:    
        if len(str((myvar))) <= 10 and len(str((myvar))) > 9:
            entry = cursor.execute(f"SELECT * from STUDENT where STU_ID = {myvar}")
            conn.commit()
            if entry != 0:
                #fetching data from database
                cursor.execute(f"SELECT STU_NAME from STUDENT where STU_ID = {myvar}")
                fetchname = cursor.fetchone()
                
                cursor.execute(f"SELECT STU_ID from STUDENT where STU_ID = {myvar}")
                fetchid = cursor.fetchone()
                
                cursor.execute(f"SELECT STU_MAIL from STUDENT where STU_ID = {myvar}")
                fetchmail = cursor.fetchone()
                
                screen1 = Tk()
                screen1.title("Student Data")
                screen1.geometry('600x600')
                main_title = Label(screen1, text='Displaying Student Data', font=('Arial', 26), fg='red', background="bisque")
                main_title.place(x=120, y=0)

                #IMAGE DETECTION
                #             frame = Frame(screen1, width=600, height=400)
                #             frame.pack()
                #             frame.place(anchor='center', relx=0.5, rely=0.5)
                # 
                #             # Create an object of tkinter ImageTk
                #             img = ImageTk.PhotoImage(Image.open("images.jpg"))
                # 
                #             # Create a Label Widget to display the text or Image
                #             label = Label(image = img)
                #             label.pack()


                namelabel = Label(screen1, text='Student Name: ', font=('Arial', 20), fg='red')
                namelabel.place(x=50, y=300)
                disp_name = Label(screen1, text=fetchname, font=('Arial', 20), fg='red')
                disp_name.place(x=260, y=300)
                idlabel = Label(screen1, text='Student ID: ', font=('Arial', 20), fg='red')
                idlabel.place(x=50, y=340)
                disp_id = Label(screen1, text=fetchid , font=('Arial', 20), fg='red')
                disp_id.place(x=260, y=340)
                maillabel = Label(screen1, text='Guardian mail: ', font=('Arial', 20), fg='red')
                maillabel.place(x=50, y=380)
                disp_mail = Label(screen1, text=fetchmail, font=('Arial', 20), fg='red')
                disp_mail.place(x=260, y=380)
                
                StartCheck = Label(screen1, text='Start Checkup: ', font=('Arial', 20), fg='red')
                StartCheck.place(x=50, y=420)
                il = Button(screen1, text='Start',font=('Arial', 16), fg='red', background="white", command = start)
                il.place(x=260, y=420)
                ts = Label(screen1, text='Previous Data: ', font=('Arial', 20), fg='red')
                ts.place(x=50, y=460)
                ig = Button(screen1, text='Previous record',font=('Arial', 16), fg='red', background="white", command = prevrecords)
                ig.place(x=260, y=460)
                
                #PREVIOUS RECORD
                def prevrecords():
                    screen1 = Tk()
                    screen1.title("Student Previous Data")
                    screen1.geometry('600x600')

                    s_name = Label(screen1, text='Student Name: ', font=('Arial', 20), fg='red')
                    s_name.place(x=50, y=300)
                    name_out = Label(screen1, text=fetchname, font=('Arial', 20), fg='red')
                    name_out.place(x=260, y=300)

                    s_id = Label(screen1, text='Student ID: ', font=('Arial', 20), fg='red')
                    s_id.place(x=50, y=340)
                    id_out = Label(screen1, text=fetchid, font=('Arial', 20), fg='red')
                    id_out.place(x=260, y=340)

                    sen1 = Label(screen1, text='SPO2: ', font=('Arial', 20), fg='red')
                    sen1.place(x=50, y=380)
                    cursor.execute(f"SELECT SPO2 from SENSORDATA where STU_ID = {myvar}")
                    fetchspo2 = cursor.fetchone()
                    sen1_out = Label(screen1, text=fetchspo2, font=('Arial', 20), fg='red')
                    sen1.place(x=260, y=380)

                    sen2 = Label(screen1, text='TEMPERATURE: ', font=('Arial', 20), fg='red')
                    sen2.place(x=50, y=380)
                    cursor.execute(f"SELECT TEMP from SENSORDATA where STU_ID = {myvar}")
                    fetchtemp = cursor.fetchone()
                    sen2_out = Label(screen1, text=fetchtemp, font=('Arial', 20), fg='red')

                    sen2_out.place(x=260, y=380)
                    sen3 = Label(screen1, text='PULSE: ', font=('Arial', 20), fg='red')
                    sen3.place(x=50, y=380)
                    cursor.execute(f"SELECT PULSE from SENSORDATA where STU_ID = {myvar}")
                    fetchpulse = cursor.fetchone()
                    sen3_out = Label(screen1, text=fetchspo2, font=('Arial', 20), fg='red')
                    sen3_out.place(x=260, y=380)

                #SENSOR's START READING
                def StartReading():
                    screen = Tk()
                    screen.title("Student Checkup")
                    screen.geometry('600x600')
                    tq = Label(screen, text='Sensor 1:', font=('Arial', 20), fg='red', background="bisque")
                    tq.place(x=50, y=150)
                    iq = Button(screen, text='start',font=('Arial', 16), fg='red', background="white", command = Communicate)
                    iq.place(x=200, y=150)
                    tq = Label(screen, text='Sensor Data:', font=('Arial', 20), fg='red', background="bisque")
                    tq.place(x=400, y=150)
                    tw = Label(screen, text='Sensor 2: ', font=('Arial', 20), fg='red', background="bisque")
                    tw.place(x=50, y=200)
                    iw = Button(screen, text='Start',font=('Arial', 16), fg='red', background="white", command = Communicate1)
                    iw.place(x=200, y=200)
                    tq = Label(screen, text='Sensor Data:', font=('Arial', 20), fg='red', background="bisque")
                    tq.place(x=400, y=200)
                    te = Label(screen, text='Sensor 3:', font=('Arial', 20), fg='red', background="bisque")
                    te.place(x=50, y=250)
                    ie = Button(screen, text='Start',font=('Arial', 16), fg='red', background="white", command = Communicate2)
                    ie.place(x=200, y=250)
                    tq = Label(screen, text='Sensor Data:', font=('Arial', 20), fg='red', background="bisque")
                    tq.place(x=400, y=250)
                    tr = Label(screen, text='Sensor 4: ', font=('Arial', 20), fg='red', background="bisque", command = Communicate3)
                    tr.place(x=50, y=300)
                    ir = Button(screen, text='Start',font=('Arial', 16), fg='red', background="white")
                    ir.place(x=200, y=300)
            else:
                messagebox.showerror("Error 404", "Entered ID does not exist")
        elif len(str((myvar))) > 10 or len(str((myvar))) < 10:
            messagebox.showerror("Error","Entered ID of " + str(len(str(myvar))) + " digit is Invalid")
    elif myvar.isdigit() == False:
        messagebox.showerror("Error", "Entered ID is Invalid")
    
def Addnew():
    screen = Tk()
    screen.title("New Student Entry")
    screen.geometry('600x600')

    def submit():
        path = f"/home/pi/Datasets_FinalProj/{str(entry2.get())}"
        os.mkdir(path)
        cursor.execute("INSERT INTO STUDENT(STU_IMAGE, STU_ID, STU_NAME, STU_MAIL) VALUES (path, entry2.get(), entry1.get(), entry3.get())")
        conn.commit()
        
    inputname = Label(screen, text='Enter Student Name: ', font=('Arial', 20), fg='red', background="bisque")
    inputname.place(x=30, y=100)
    inputid = Label(screen, text='Enter Student ID: ', font=('Arial', 20), fg='red', background="bisque")
    inputid.place(x=30, y=150)
    inputmail = Label(screen, text='Enter Student Email-ID: ', font=('Arial', 20), fg='red', background="bisque")
    inputmail.place(x=30, y=200)

    entry1 = Entry(screen, font=('Arial', 20), width=10)#, textvariable = e_name)
    entry1.place(x=350, y=100)
    entry1.get()
    entry2 = Entry(screen, font=('Arial', 20), width=10)#textvariable = e_id, )
    entry2.place(x=350, y=150)
    entry2.get()
    entry3 = Entry(screen, font=('Arial', 20), width=10)#, textvariable = e_mail)
    entry3.place(x=350, y=200)

    submitbutton = Button(screen, text='SUBMIT', font=('Arial', 20), fg='red', background="white", command = submit)
    submitbutton.place(x=430, y=250)




    
def Senddata():
    Print("Send the data to the database")
    
    
def Communicate():
    print("send command to raspberry pi")

def Communicate1():
    print("send command1 to raspberry pi")

def Communicate2():
    print("send command2 to raspberry pi")

def Communicate3():
    print("send command3 to raspberry pi")

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
b = Button(screen, text='OK', font=('Arial', 14), fg='red', background="white", command = ExistingStudent)
b.place(x=430, y=210)
t5 = Label(screen, text='Add New Student ', font=('Arial', 14),  fg='black', background="bisque")
t5.place(x=235, y=315)
b = Button(screen, text='OK', font=('Arial', 14), fg='red', background="white", command = Addnew)
b.place(x=430, y=310)

screen.mainloop()

# ======== DATABASE PROGRAM ==========================================================================


# partypopper = chr(0x1f389)

# while True:
	# print("==== Choose an Option ====")
	# print("1. Add a new Student")
	# print("2. Add values")
	# print("3. Show Values")
	# print("PRESS 0 TO EXIT \n")
	# i = int(input("Option: "))

	# #Exiting the program
	# if i == 0:
		# print("\n ==> BYE .......")
		# break

	# #for a new student
	# elif i == 1:
		# print("\n * ====== NEW ENTRY MENU ====== *")
		# rno = input("--> Student ID: ")
		# path = f'/home/pi/testing/{rno}'
		# os.mkdir(path)
		# name = input("--> Student Name: ")
		# mail = input("--> Enter a valid e-mail address: ")
		# try:
			# cursor.execute("INSERT INTO STUDENT (STU_IMAGE, STU_ID, STU_NAME, STU_MAIL) VALUES (%s, %s, %s, %s)", (path, rno, name, mail))
			# conn.commit()
			# print(f"$$ New Entry Added Sucessfully {partypopper} {partypopper} \n")
		# except TypeError:
			# print("==*= Invalid input! Try again =*==")
		# except  FileExistsError:
			# print("==*= File already exists! Try something else =*==")

	# #sensor input based on the above rno
	# elif i == 2:
		# print("\n * ===== VALUES INSERTION ====== *")
		# rno = input("--> Enter an existing roll no.:")
		# try:
			# now = datetime.now()
			# formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
			# time = formatted_date
			# sen1 = input("--> Enter the first value: ")
			# sen2 = input("--> Enter the second value: ")
			# sen3 = input("--> Enter the third value: ")
			# cursor.execute("INSERT INTO SENSORDATA (STU_ID, TEST_TIME, SEN1, SEN2, SEN3) VALUES (%s, %s, %s, %s, %s)", (rno, time, sen1, sen2, sen3))
			# conn.commit()
		# except TypeError:
			# print("==*= Invalid Input! Try again =*==")

	# elif i == 3:
		# print("\n * ====== LAST RECORD ====== *")
		# rno = input("--> Enter the roll no. for the last value: ")
		# cursor.execute("SELECT * FROM SENSORDATA where STU_ID = %s", (rno))
		# output = cursor.fetchone()
		# print(output)
		# conn.commit()

# #exitting
# cursor.close()
# conn.close()
