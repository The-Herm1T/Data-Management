from tkinter import *
import pandas as pd
import sqlite3
from PIL import ImageTk,Image

win=Tk()
win.title("Student Management System")
win.geometry("350x350")
myimg=ImageTk.PhotoImage(Image.open("c:/Users/Pawan/Downloads/pcn.png"))
def insertf():
    win.withdraw()
    global ins
    ins=Tk()
    ins.title('Insert a Record')
    ins.geometry("300x300")

    def btn():
        ins.destroy()
        win.deiconify()

    def submit():
        conn = sqlite3.connect('management.db')
        c = conn.cursor()
        c.execute("INSERT INTO students VALUES (:name, :father_name, :gender, :mobile, :email)",
			{
				'name': name.get(),
				'father_name': father_name.get(),
				'gender': gender.get(),
				'mobile': mobile.get(),
                                'email': email.get()
			})
        conn.commit()
        conn.close()



        
        name.delete(0, END)
        father_name.delete(0, END)
        gender.delete(0, END)
        mobile.delete(0, END)
        email.delete(0, END)
        
        

    name = Entry(ins, width=30)
    name.grid(row=0, column=1, pady=(10, 0))
    father_name = Entry(ins, width=30)
    father_name.grid(row=1, column=1)
    gender= Entry(ins, width=30)
    gender.grid(row=2, column=1)
    mobile = Entry(ins, width=30)
    mobile.grid(row=3, column=1)
    email = Entry(ins, width=30)
    email.grid(row=4, column=1)

    name_label = Label(ins, text="Name")
    name_label.grid(row=0, column=0, padx=(20,5), pady=(10,0),sticky=E)
    father_name_label = Label(ins, text="Father's Name")
    father_name_label.grid(row=1, column=0, padx=(20,5), pady=2,sticky=E)
    gender_label = Label(ins, text="Gender")
    gender_label.grid(row=2, column=0, padx=(20,5), pady=2,sticky=E)
    mobile_label = Label(ins, text="Mobile")
    mobile_label.grid(row=3, column=0, padx=(20,5), pady=2,sticky=E)
    email_label = Label(ins, text="Email")
    email_label.grid(row=4, column=0, padx=(20,5), pady=2,sticky=E)


    btn1 = Button(ins, text="Back to Main",command=btn)
    btn1.grid(row=6, column=0,columnspan=2)
    btn2 = Button(ins, text="Submit",command=submit)
    btn2.grid(row=5, column=0,columnspan=2,pady=10)

    


    

       
    

def searchf():
    win.withdraw()
    global sea
    sea=Tk()
    sea.title('Search Record')
    sea.geometry("300x300")
    def btn():
        sea.destroy()
        win.deiconify()
    def search():
        def ok():
            top.destroy()
            sea.deiconify()
        sea.withdraw()
        top=Toplevel()
        top.title('Searched Data')
        top.geometry("300x300")
        conn = sqlite3.connect('management.db')
        c = conn.cursor()
        c.execute("SELECT * from students WHERE oid = " + uid.get())
        record=c.fetchall()
        for rec in record:
            a=rec[0]
            b=rec[1]
            c=rec[2]
            d=rec[3]
            e=rec[4]
        query_lab1 = Label(top,text="Name   :")
        query_lab1.grid(row=1,column=1)
        query_lab2 = Label(top,text=a)
        query_lab2.grid(row=1,column=2)
        query_lab3 = Label(top,text="Father's Name   :")
        query_lab3.grid(row=2,column=1)
        query_lab4= Label(top,text=b)
        query_lab4.grid(row=2,column=2)
        query_lab5 = Label(top,text="Gender   :")
        query_lab5.grid(row=3,column=1)
        query_lab6= Label(top,text=c)
        query_lab6.grid(row=3,column=2)
        query_lab7 = Label(top,text="Mobile Number   :")
        query_lab7.grid(row=4,column=1)
        query_lab8= Label(top,text=d)
        query_lab8.grid(row=4,column=2)
        query_lab9 = Label(top,text="Email ID   :")
        query_lab9.grid(row=5,column=1)
        query_lab0= Label(top,text=e)
        query_lab0.grid(row=5,column=2)
        
        btn=Button(top,text="Close Window",command=ok).grid(row=6,column=2)
        
        
        
        uid.delete(0, END)
        conn.commit()
        conn.close()
        
    uid = Entry(sea, width=30)
    uid.grid(row=0, column=1, pady=(10, 0))
    uid_label = Label(sea, text="Enter the ID")
    uid_label.grid(row=0, column=0, padx=(20,5),pady=(10, 0))
    btn1 = Button(sea, text="Back to Main",command=btn)
    btn1.grid(row=3, column=0,columnspan=2)
    btn2 = Button(sea, text="Search",command=search)
    btn2.grid(row=2, column=0,columnspan=2,pady=10)
    

def displayf():
    win.withdraw()
    global dis,record
    dis=Tk()
    dis.title('All Records')
    dis.geometry("600x600")
    def btn():
        dis.destroy()
        win.deiconify()

    conn = sqlite3.connect('management.db')
    c = conn.cursor()

    c.execute("SELECT * from students")
    record = c.fetchall()
    print_rec=''
    for rec in record:
        print_rec += str(rec) + "\n"  
    label = Label(dis, text=print_rec,font=("Arial",10))
    label.grid(row=0, column=0,columnspan=2,padx=25)
    btn2 = Button(dis, text="Back",command=btn)
    btn2.grid(row=1, column=0,columnspan=2)

    conn.commit()
    conn.close()

    

def deletef():
    win.withdraw()
    global dele
    dele=Tk()
    dele.title('Delete Record')
    dele.geometry("300x300")
    def btn():
        dele.destroy()
        win.deiconify()
    def delete():
        conn = sqlite3.connect('management.db')
        c = conn.cursor()
        c.execute("DELETE from students WHERE oid = " + uid.get())
        uid.delete(0, END)
        conn.commit()
        conn.close()
        
    uid = Entry(dele, width=30)
    uid.grid(row=0, column=1, padx=20, pady=(10, 0))
    uid_label = Label(dele, text="Enter the ID")
    uid_label.grid(row=0, column=0,padx=(20,0), pady=(10, 0))
    btn1 = Button(dele, text="Back to Main",command=btn)
    btn1.grid(row=3, column=0,columnspan=2)
    btn2 = Button(dele, text="Delete",command=delete)
    btn2.grid(row=2, column=0,columnspan=2,pady=10)
   
def updatef():
    win.withdraw()
    global up
    up=Tk()
    up.title('Update Record')
    up.geometry("300x300")
    def btn():
        up.destroy()
        win.deiconify()
    def update():
            conn = sqlite3.connect('management.db')
            c = conn.cursor()

            record_id = did.get()

            c.execute("""UPDATE students SET
		name = :namel,
		father_name = :father,
		gender = :gen,
		mobile= :mob,
		email= :emal
                WHERE oid = :oid""",
		{
		'namel': name.get(),
		'father': father_name.get(),
		'gen': gender.get(),
		'mob': mobile.get(),
                'emal':email.get(),
		'oid': record_id
		})

            conn.commit()
            conn.close()
            did.delete(0, END)
            ws.destroy()
            up.deiconify()    
    def contin():
        up.withdraw()
        global ws
        ws=Tk()
        ws.title('Selected Record')
        ws.geometry("300x300")

        conn = sqlite3.connect('management.db')
        c = conn.cursor()
        record_id = did.get()
        c.execute("SELECT * FROM students WHERE oid = " + record_id)
        records = c.fetchall()
            

        
        

        global name
        global father_name
        global gender
        global mobile
        global email
        
        name = Entry(ws, width=30)
        name.grid(row=0, column=1, padx=20, pady=(10, 0))
        father_name = Entry(ws, width=30)
        father_name.grid(row=1, column=1)
        gender= Entry(ws, width=30)
        gender.grid(row=2, column=1)
        mobile= Entry(ws, width=30)
        mobile.grid(row=3, column=1)
        email= Entry(ws, width=30)
        email.grid(row=4, column=1)

        name_label = Label(ws, text="UID")
        name_label.grid(row=0, column=0, pady=(10, 0))
        father_name_label = Label(ws, text="First Name")
        father_name_label.grid(row=1, column=0)
        gender_label = Label(ws, text="Last Name")
        gender_label.grid(row=2, column=0)
        mobile_label = Label(ws, text="Department")
        mobile_label.grid(row=3, column=0)
        email_label = Label(ws, text="Department")
        email_label.grid(row=4, column=0)

        for record in records:
            name.insert(0, record[0])
            father_name.insert(0, record[1])
            gender.insert(0, record[2])
            mobile.insert(0, record[3])
            email.insert(0, record[4])
        conn.commit()
        conn.close()
        
        btn2 = Button(ws, text="Update",command=update)
        btn2.grid(row=5, column=0,columnspan=2,pady=10)
        
    global did
    did = Entry(up, width=30)
    did.grid(row=0, column=1, padx=20, pady=(10, 0))
    uid_label = Label(up, text="Enter the ID")
    uid_label.grid(row=0, column=0, pady=(10, 0))
    btn1 = Button(up, text="Back to Main",command=btn)
    btn1.grid(row=3, column=0,columnspan=2)
    btn2 = Button(up, text="Continue",command=contin)
    btn2.grid(row=2, column=0,columnspan=2,pady=10)
    

def clearf():
    conn = sqlite3.connect('management.db')
    c = conn.cursor()
    c.execute("""DROP TABLE students""")
    
    conn.commit()
    c.execute("""CREATE TABLE students (
                name text, 
		father_name text,
		gender text,
		mobile text,
		email text
		)""")
    conn.commit()
    conn.close()

label1=Label(win,font=("Times New Roman",20),image=myimg)
insert=Button(win,text="Insert Data",command=insertf)
search=Button(win,text="Search Data",command=searchf)
display=Button(win,text="Display Data",command=displayf)
delete=Button(win,text="Delete Data",command=deletef)
clear=Button(win,text="Clear All Data",command=clearf)
update=Button(win,text="Update Data",command=updatef)
label1.grid(row=1,column=0,columnspan=2,padx=15,pady=5,ipadx=10,ipady=10)
insert.grid(row=2,column=0,padx=10,pady=5,ipadx=24,ipady=20,sticky=E)
search.grid(row=2,column=1,padx=10,pady=5,ipadx=20,ipady=20,sticky=W)
display.grid(row=3,column=0,padx=10,pady=5,ipadx=20,ipady=20,sticky=E)
delete.grid(row=3,column=1,padx=10,pady=5,ipadx=21,ipady=20,sticky=W)
clear.grid(row=4,column=1,padx=10,pady=5,ipadx=16,ipady=20,sticky=W)
update.grid(row=4,column=0,padx=10,pady=5,ipadx=20,ipady=20,sticky=E)










win.mainloop()
