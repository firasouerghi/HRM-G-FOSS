
try :
    import os
    import tkinter
    from tkinter import *
    from tkinter import messagebox, ttk
    import glob
    from PIL import *
    from PIL import ImageTk ,Image
    import webbrowser
    import datetime
    import fbchat

    import matplotlib.pyplot as plt

    from tkinter import *
    import matplotlib

    matplotlib.use('TkAgg')
    import numpy as np
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure

except ImportError :
    print("No Module Found")
    raise
finally:
    import tkinter
    from tkinter import *
    from tkinter import messagebox, ttk
    import glob
    from PIL import *
    from PIL import ImageTk
    import webbrowser
    import os
    import fbchat

    import matplotlib.pyplot as plt

    from tkinter import *
    import matplotlib

    matplotlib.use('TkAgg')
    import numpy as np
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
try :
    import sqlite3
except ImportError :
    print ("NO module found")
    raise
finally:
    import sqlite3
try:
    import time
except ImportError :
    print("No Modile Found")
    raise
finally:
    import time
try:
    from BackEnd import DataBase
except ImportError as e :
    print("error importing Module{0}".format(e.strerro))
finally:
    from BackEnd import DataBase

try :
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
except ImportError as e :
    print("error importing Module{0}".format(e.strerro))
finally:
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
try :
    from reportlab.lib.enums import TA_JUSTIFY
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
except ImportError as e:
    print("error importing Module{0}".format(e.strerro))
finally:
    from reportlab.lib.enums import TA_JUSTIFY
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch

con = sqlite3.connect("agenda.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS agenda (id INTEGER PRIMARY KEY  AUTOINCREMENT , date DATE ,event VARCHAR(10000)) ")
con.commit()
con.close()
con = sqlite3.connect("Notation.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS nota (id INTEGER PRIMARY KEY  AUTOINCREMENT , date DATE ,notation VARCHAR(10000)) ")
con.commit()
con.close()

dbName="G2FOSSMEMBERS"
DB=DataBase(dbName)
t="We’re a group of engineering students who share the "+"\n"+"belief that open source software–technology built with "+"\n"+"code that is open for view, use, and modification – is the"+"\n"+" engine that empower innovation.G2FOSS club is open to"+"\n"+" all students of all backgrounds and disciplines"+"\n"+" who are interested in free and open source software ."+"\n"+"Our goal is to foster a community of makers,"+"\n"+" who want to solve problems, explore their professional"+"\n"+" world and learn about the latest open source technologies."+"\n"+"Are you excited to explore the open source world ?"+"\n"+"#Come_to_learn_about_open_source "+"\n"+"#Join_us_to_unlock_your_curiosity"

def insertCommand() :
    DB.insert(e1entry.get(),e2entry.get(),e3entry.get(),e4entry.get(),e5entry.get(),
              str(combo5entry.get())+"-"+str(combo6entry.get())+"-"+str(combo7entry.get()),combo1entry.get(),combo2entry.get(),
              combo4entry.get(),combo3entry.get(),picpath.get(),efbidentry.get())
    L1.delete(0, END)
    a = (e1entry.get(),e2entry.get(),e3entry.get(),e4entry.get(),e5entry.get(),
         str(combo5entry.get())+"-"+str(combo6entry.get())+"-"+str(combo7entry.get()),str(combo1entry.get()),str(combo2entry.get()),
         str(combo4entry.get()),str(combo3entry.get()))
    L1.insert(END, a)
    messagebox.showinfo("Add "," Member Added successfully")


def viewCommand() :
    L1.delete(0, END)
    for row in DB.view():
        L1.insert(END, row)
def refresh():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    efid.delete(0,END)

    combo.set("membersimg/defaultPic.jpg")
    combo1.set("Choose")
    combo2.set("Choose")
    combo3.set("Choose")
    combo4.set("Choose")
    combo5.set("Day")
    combo6.set("Month")
    combo7.set("Year")
    a = ImageTk.PhotoImage(file="membersimg/defaultPic.jpg")
    canvas.delete(ALL)
    canvas.create_image(0, 0, anchor=NW, image=a)
    canvas.image = a
    canvas.update()
def getSelectedRow(event):
    global selectedTuple
    index=L1.curselection()[0]
    selectedTuple=L1.get(index)

    e1.delete(0,END)
    e1.insert(END,selectedTuple[1])
    e2.delete(0,END)
    e2.insert(END,selectedTuple[2])
    e3.delete(0,END)
    e3.insert(END,selectedTuple[3])
    e4.delete(0, END)
    e4.insert(END, selectedTuple[4])
    e5.delete(0,END)
    e5.insert(END,selectedTuple[5])
    efid.delete(0,END)
    efid.insert(END,selectedTuple[12])

    combo.set(selectedTuple[11])
    combo1.set(selectedTuple[7])
    combo2.set(selectedTuple[8])
    combo3.set(selectedTuple[10])
    combo4.set(selectedTuple[9])
    combo5.set(selectedTuple[6][0:2])
    combo6.set(selectedTuple[6][3:5])
    combo7.set(selectedTuple[6][6:11])
    a = ImageTk.PhotoImage(file=selectedTuple[11])
    canvas.delete(ALL)
    canvas.create_image(0, 0, anchor=NW, image=a)
    canvas.image = a
    canvas.update()

def delete():
    DB.delete(selectedTuple[0])
    messagebox.showinfo("Delete "," Member deleted successfully")


def update():
    DB.update(selectedTuple[0],e1entry.get(),e2entry.get(),e3entry.get(),e4entry.get(),e5entry.get(),str(combo5entry.get())+"-"+str(combo6entry.get())+"-"+str(combo7entry.get()),combo1entry.get(),combo2entry.get(),combo4entry.get(),combo3entry.get(),picpath.get(),efbidentry.get())
    messagebox.showinfo("Update "," Member updated successfully")
def ret():
    secondFrame.destroy()
    bb.destroy()
    fb.destroy()
    fstPage()

def getimg(event):
    if picpath.get()!="":
        a=ImageTk.PhotoImage(file=str(picpath.get()))
        canvas.delete(ALL)
        canvas.create_image(0, 0, anchor=NW, image=a)
        canvas.image = a
        canvas.update()
    else:
        a = ImageTk.PhotoImage(file="img/defaultPic.jpg")
        canvas.delete(ALL)
        canvas.create_image(0, 0, anchor=NW, image=a)
        canvas.image = a
        canvas.update()

def Dash():
    for widget in frane.winfo_children():
        widget.destroy()


    global picpath, combo1entry, combo2entry, combo3entry, combo4entry, combo5entry, combo6entry, combo7entry, combo, combo1, combo2, combo3, combo4, combo5, combo6, combo7
    picpath = StringVar()

    combo = ttk.Combobox(frane, width=12, font=("Helvetica", 10, "bold italic"), textvariable=picpath)
    combo.bind("<<ComboboxSelected>>", getimg)
    combo['values'] = [i for i in glob.glob("membersimg/*")]
    # combo.insert(END,["File Path"])
    combo.set('membersimg/defaultPic.jpg')
    combo1entry = StringVar()
    combo1 = ttk.Combobox(frane, width=12, font=("Helvetica", 10, "bold italic"), textvariable=combo1entry)

    combo1['values'] = (
    "Choose", "Ariana", "Ben Arous", "Béja", "Bizerte", "Gabès", "Gafsa", "Jendouba", "Kairouan", "Kasserine", "Kébili",
    "Le Kef", "Mahdia", "La Manouba", "Médenine", "Monastir", "Nabeul", "Sfax", "Sidi Bouzid", "Siliana", "Sousse",
    "Tataouine", "Tozeur", "Tunis", "Zaghouan")
    combo1.current(0)

    # combo1.insert(END,["Choose"])
    combo2entry = StringVar()

    combo2 = ttk.Combobox(frane, width=12, font=("Helvetica", 10, "bold italic"), textvariable=combo2entry)

    combo2['values'] = (
    "Choose", "Telecom", "IT", "electrical", "MINDS", "TA", "Hydraulical", "Mecanical", "Industrial", "Civil", "Master",
    "PHD")
    # combo2.insert(END,["Choose"])
    combo2.current(0)
    combo3entry = StringVar()

    combo3 = ttk.Combobox(frane, width=12, font=("Helvetica", 10, "bold italic"), textvariable=combo3entry)

    combo3['values'] = ("Choose", "New Member", "Old Member", "Admin Member", "Supper Member")
    combo3.current(0)

    # combo3.insert(END,["Choose"])
    combo4entry = StringVar()

    combo4 = ttk.Combobox(frane, width=20, font=("Helvetica", 10, "bold italic"), textvariable=combo4entry)

    combo4['values'] = ("Choose", "Embedded electronics Workshop", "Development Workshop", "Security Workshop")
    combo4.current(0)
    combo5entry = StringVar()
    combo5 = ttk.Combobox(frane, width=4, font=("Helvetica", 10, "bold italic"), textvariable=combo5entry)
    combo5['values'] = (
    "Day", '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
    '19', '20', '21', '22',
    '23', '24', '25', '26', '27', '28', '29', '30', '31')
    combo5.current(0)
    combo6entry = StringVar()
    combo6 = ttk.Combobox(frane, width=6, font=("Helvetica", 10, "bold italic"), textvariable=combo6entry)
    combo6['values'] = ("Month", '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
    combo6.current(0)
    combo7entry = StringVar()
    combo7 = ttk.Combobox(frane, width=5, font=("Helvetica", 10, "bold italic"), textvariable=combo7entry)
    combo7['values'] = (
    "Year", '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002',
    '2003',
    '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
    '2018')
    combo7.current(0)
    a = ImageTk.PhotoImage(file="membersimg/defaultPic.jpg")
    global canvas
    canvas = Canvas(frane, width=100, height=100, bg='#000000')
    canvas.create_image(0, 0, anchor=NW, image=a)
    canvas.image = a

    canvas.grid(row=0, column=0)
    combo.grid(row=0, column=1)

    b9 = Button(frane, text="Insert", width=13, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', command=insertCommand)
    b10 = Button(frane, text="Edit", width=13, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', command=update)
    b11 = Button(frane, text="Delete", width=13, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', command=delete)
    b12 = Button(frane, text="View", width=13, font=("Helvetica", 10, "bold italic"), bg='#EEE8AA',command=viewCommand)
    b13 = Button(frane, text="Refresh", width=13, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', command=refresh)
    b9.grid(row=16, column=0, padx=5, pady=25)
    b10.grid(row=16, column=1, padx=5, pady=25)
    b11.grid(row=16, column=2, padx=5, pady=25)
    b12.grid(row=16, column=3, padx=5, pady=25)
    b13.grid(row=16, column=4, padx=5, pady=25)

    global L1
    L1 = Listbox(frane, height=10, width=120, font=("Helvetica", 10, "bold italic"))  # NOT A Text widget
    s1 = Scrollbar(frane, orient='vertical', width=20, highlightcolor='red')
    s2 = Scrollbar(frane, orient=HORIZONTAL, width=20)

    s1 = Scrollbar(frane, orient='vertical', width=20, highlightcolor='red')

    L1.configure(yscrollcommand=s1.set)
    L1.configure(xscrollcommand=s2.set)
    s1.configure(command=L1.yview)
    s2.configure(command=L1.xview)
    # to return the index of the selected row
    L1.bind("<<ListboxSelect>>", getSelectedRow)

    global e1entry, e2entry, e3entry, e4entry, e5entry,efbidentry ,e1, e2, e3, e4, e5,efid
    l1 = Label(frane, text='First Name', font=("Helvetica", 10, "bold italic"), bg='#EEE8AA',width=13)
    e1entry = StringVar()
    e1 = Entry(frane, textvariable=e1entry, width=13, font=("Helvetica", 10, "bold italic"))
    l2 = Label(frane, text='Last Name', font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', width=13)

    e2entry = StringVar()
    e2 = Entry(frane, textvariable=e2entry, width=13, font=("Helvetica", 10, "bold italic"))
    l3 = Label(frane, text='cin', font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', width=13)

    e3entry = StringVar()
    e3 = Entry(frane, textvariable=e3entry, width=13, font=("Helvetica", 10, "bold italic"))
    l4 = Label(frane, text='email @', font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', width=13)

    e4entry = StringVar()
    e4 = Entry(frane, textvariable=e4entry, width=13, font=("Helvetica", 10, "bold italic"))
    l5 = Label(frane, text='Phone', font=("Helvetica", 10, "bold italic"), bg='#EEE8AA',width=13)

    e5entry = StringVar()
    e5 = Entry(frane, textvariable=e5entry, width=13, font=("Helvetica", 10, "bold italic"))
    l6 = Label(frane, text='Physical @', font=("Helvetica", 10, "bold italic"), bg='#EEE8AA',width=13)
    efbidentry=StringVar()
    efid=Entry(frane,textvariable=efbidentry, width=13, font=("Helvetica", 10, "bold italic"))

    lfbid = Label(frane, text='Facebook ID', font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', width=13)

    l7 = Label(frane, text='Study Section', font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', width=13)

    l8 = Label(frane, text='Status', font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', width=13)

    l9 = Label(frane, text='Workshop', font=("Helvetica", 10, "bold italic"),bg='#EEE8AA', width=13)
    l10 = Label(frane, text='Birthday', font=("Helvetica", 10, "bold italic"), bg='#EEE8AA',width=13)

    l1.grid(row=1, column=0, pady=25, padx=5)
    e1.grid(row=1, column=1, pady=25, padx=5)

    l2.grid(row=1, column=2, pady=25, padx=5)
    e2.grid(row=1, column=3, pady=25, padx=5)

    l3.grid(row=1, column=4, pady=25, padx=5)
    e3.grid(row=1, column=5, pady=25, padx=5)
    l4.grid(row=2, column=0, pady=25, padx=5)
    e4.grid(row=2, column=1, pady=25, padx=5)

    l5.grid(row=2, column=2, pady=25, padx=5)
    e5.grid(row=2, column=3, pady=25, padx=5)
    l6.grid(row=2, column=4, pady=25, padx=5)

    combo1.grid(row=2, column=5, pady=25, padx=5)

    l7.grid(row=3, column=0, pady=25, padx=10)
    combo2.grid(row=3, column=1, padx=10, pady=25)

    l8.grid(row=3, column=2, pady=25, padx=10)
    combo3.grid(row=3, column=3, padx=10, pady=25)

    l9.grid(row=3, column=4, pady=25, padx=10)
    combo4.grid(row=3, column=5, pady=25, padx=10)
    l10.grid(row=4, column=0, pady=25, padx=10)
    combo5.grid(row=4, column=1, pady=25, padx=10)
    combo6.grid(row=4, column=2, pady=25, padx=10)
    combo7.grid(row=4, column=3, pady=25, padx=10)
    lfbid.grid(row=4, column=4, pady=25, padx=10)
    efid.grid(row=4, column=5, pady=25, padx=10)

    L1.grid(row=5, column=0, rowspan=10, columnspan=20)
    s1.grid(row=5, column=21, rowspan=10)
    s2.grid(row=15, column=3)


def Notification():
    for widget in frane.winfo_children():
        widget.destroy()

    nl=Listbox(frane,width=60,height=15,font=("Helvetica", 10, "bold italic"))
    nb=Listbox(frane,width=55,height=15,font=("Helvetica", 10, "bold italic"))

    s1 = Scrollbar(frane, orient='vertical', width=20, highlightcolor='red')
    s2 = Scrollbar(frane, orient='vertical', width=20, highlightcolor='red')
    nl.configure(yscrollcommand=s1.set)
    s1.configure(command=nl.yview)
    nb.configure(yscrollcommand=s2.set)
    s2.configure(command=nb.yview)
    l1=Label(frane,width=60,text="Chesk Anniversary ",bg='#EEE8AA',font=("Helvetica", 10, "bold italic"))
    l2=Label(frane,width=55,text="Chesk Agenda",bg='#EEE8AA',font=("Helvetica", 10, "bold italic"))
    nl.configure(yscrollcommand=s1.set)
    nb.configure(yscrollcommand=s2.set)
    s1.configure(command=nl.yview)
    s1.configure(command=nb.yview)
    greatting=Button(frane,text="Send Greatings",font=("Helvetica", 10, "bold italic"),width=13,bg='#EEE8AA',command=sendG)
    checked=Button(frane,text="Checked",font=("Helvetica", 10, "bold italic"),width=13,bg='#EEE8AA',command=check)
    l1.grid(row=0, column=0,pady=25)
    l2.grid(row=0,column=2,pady=25)
    nl.grid(row=1,column=0)
    s1.grid(row=1,column=1)
    nb.grid(row=1,column=2)
    s2.grid(row=1,column=3)
    greatting.grid(row=3,column=0,pady=25)
    checked.grid(row=3,column=2,pady=25)
    nl.delete(0, END)
    for x,y in anniversaryList.items() :
        nl.insert(END, x)

    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM agenda")
    row = cur.fetchall()
    for event in row:
        nb.insert(END, event)
    con.close()

def check() :
    b1.configure(text='Notification',bg='#EEE8AA',font=("Helvetica", 10, "bold italic"))
def sendG ():

    print(anniversaryList)

    for x, y in anniversaryList.items():
        a=client=fbchat.Client('put your email @ here ','put your password here ')
        client.send(fbchat.models.Message("Dear  "+str(x[0])+" \n Thank you so much for being such an amazing memeber of our community .\n On your special day, We just wanted you to know that we are happy to have such a wonderful G²FOSSER.\n we will remember you in our thoughts forever.We wish you all the good \nthings on your special day and may the FOSS bless you. Have a joyous birthday celebration! \nG²FOSS ENIT COMMUNITY "),str(y))
        messagebox.showinfo("Send ", "successfully sent  to %s:" % str(x[0]))
    b1.configure(text='Notification',bg='#EEE8AA',font=("Helvetica", 10, "bold italic"))



def getimgfdb(event):
        for row in DB.search("", "", str(c.get()), "", "", "", "", "", "", ""):
            lala.configure(text=row[1])
            a = ImageTk.PhotoImage(file=row[11])
            canvaso.delete(ALL)
            canvaso.create_image(0, 0, anchor=NW, image=a)
            canvaso.image = a
            canvaso.update()
def Inspections() :
    for widget in frane.winfo_children():
        widget.destroy()
    global  v1,v2,v3,canvaso,c,lala
    v1=IntVar()
    v2=IntVar()
    v3=IntVar()
    rb1 = ttk.Checkbutton(frane, text='Presence', variable=v1, width=20, onvalue=1,offvalue=0)
    rb2 = ttk.Checkbutton(frane, text='Attendance', variable=v2, width=20, onvalue=1, offvalue=0)
    rb3 = ttk.Checkbutton(frane, text='Participation', variable=v3, width=20, onvalue=1, offvalue=0)
    canvaso = Canvas(frane, width=100, height=100, bg='#000000')
    bi=Button(frane,width=20,bg='#EEE8AA', font=("Helvetica", 10, "bold italic"),text="Submit",command=submit)
    c = StringVar()
    com = ttk.Combobox(frane, width=20, font=("Helvetica", 10, "bold italic"), textvariable=c)
    com.bind("<<ComboboxSelected>>", getimgfdb)
    lala=Label(frane,width=20, bg='#EEE8AA',font=("Helvetica", 10, "bold italic"))
    com['values'] = [i[3] for i in DB.view()]
    canvaso.grid(row=0,column=0,padx=25)
    rb1.grid(row=0, column=1, padx=25)
    rb2.grid(row=0, column=2, padx=25)
    rb3.grid(row=0, column=3, padx=25)
    lala.grid(row=3, column=0, padx=25,pady=25)
    bi.grid(row=4, column=0, padx=25,pady=25)
    com.grid(row=1,column=2,padx=25)

def submit():
    cin = c.get()
    col=DB.cursor.execute("SELECT pr ,att ,par FROM G2FOSSMEMBERS WHERE cin=?",(cin,))
    for row in col :
        pr=int(row[0])
        att=int(row[1])
        par=int(row[2])
    DB.cursor.execute("UPDATE G2FOSSMEMBERS SET pr = ? , att= ? ,par = ? WHERE cin= ?",(pr+v1.get(),att+v2.get(),par+v3.get(),cin))
    DB.conection.commit()

def Agenda():

    for widget in frane.winfo_children():
        widget.destroy()
    global titleentry,agdayentry,agmonthentry,agyearentry,aglist

    archiveLabel=Label(frane,bg='#EEE8AA',text='Archive',font=("Helvetica", 10, "bold italic"),width=25)
    aglist=Listbox(frane,width=60,height=10,font=("Helvetica", 10, "bold italic"))
    sag = Scrollbar(frane, orient='vertical', width=20, highlightcolor='red')
    aglist.configure(yscrollcommand=sag.set)
    sag.configure(command=aglist.yview)
    sagv = Scrollbar(frane, orient='horizontal', width=20, highlightcolor='red')
    aglist.configure(xscrollcommand=sagv.set)
    sagv.configure(command=aglist.xview)
    ShowArchiveButton=Button(frane,bg='#EEE8AA',width=25,text="Show Archive",font=("Helvetica", 10, "bold italic"),command=showag)
    EventLabel=Label(frane,text='Event',bg='#EEE8AA',font=("Helvetica", 10, "bold italic"),width=25)
    EventTitleLabel=Label(frane,bg='#EEE8AA',text='Event Title ',font=("Helvetica", 10, "bold italic"),width=25)
    titleentry=StringVar()
    EventTytleEntry=Entry(frane,width=25,font=("Helvetica", 10, "bold italic"),textvariable=titleentry)
    EventDateLabel=Label(frane,bg='#EEE8AA',text='Date',font=("Helvetica", 10, "bold italic"),width=25)
    agdayentry = StringVar()
    comboagday = ttk.Combobox(frane, width=4, font=("Helvetica", 10, "bold italic"), textvariable=agdayentry)
    comboagday['values'] = (
        "Day", '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
        '18','19', '20', '21', '22','23', '24', '25', '26', '27', '28', '29', '30', '31')
    comboagday.current(0)
    agmonthentry = StringVar()
    comboagmonth = ttk.Combobox(frane, width=6, font=("Helvetica", 10, "bold italic"), textvariable=agmonthentry)
    comboagmonth['values'] = ("Month", '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
    comboagmonth.current(0)
    agyearentry = StringVar()
    comboagyear = ttk.Combobox(frane, width=5, font=("Helvetica", 10, "bold italic"), textvariable=agyearentry)
    comboagyear['values'] = ("Year", '2018', '2019', '2020')
    comboagyear.current(0)
    addtoagButton=Button(frane,bg='#EEE8AA',width=25,text="Add to my agenda",font=("Helvetica", 10, "bold italic"),command=add2ag)
    archiveLabel.grid(row=0,column=0,pady=20,padx=10)
    aglist.grid(row=1,column=0,rowspan=3,pady=20,padx=10)
    sag.grid(row=2,column=1,pady=20,padx=1)
    sagv.grid(row=4,column=0,pady=1,padx=1)
    ShowArchiveButton.grid(row=5,column=0,padx=20,pady=30)
    EventLabel.grid(row=0,column=2,columnspan=3,padx=20,pady=20)
    EventTitleLabel.grid(row=1,column=2,padx=20,pady=20)
    EventTytleEntry.grid(row=1,column=3,padx=20,pady=20)
    EventDateLabel.grid(row=2,column=2,columnspan=3,padx=20,pady=2)
    comboagday.grid(row=3,column=2,padx=10,pady=10)
    comboagmonth.grid(row=3,column=3,padx=10,pady=10)
    comboagyear.grid(row=3,column=4,padx=10,pady=10)
    addtoagButton.grid(row=5,column=2,columnspan=4,pady=10,padx=20)

def showag():
    aglist.delete(0,END)
    con=sqlite3.connect("agenda.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM agenda")
    for event in cur.fetchall() :
        print(event)
        aglist.insert(END,event)
    con.close()
def add2ag():
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("INSERT INTO agenda  VALUES (NULL,?,?)",(str(agdayentry.get())+"-"+str(agmonthentry.get())+"-"+str(agyearentry.get()),titleentry.get()))
    con.commit()
    con.close()
    messagebox.showinfo("agenda ","EVENT ADDED SUCCESSFULLY TO ARCHIVE")

def HRM_TOOLS():
    for widget in frane.winfo_children():
        widget.destroy()
    pvButton=Button(frane,bg='#EEE8AA',text='Report',width=13, font=("Helvetica", 10, "bold italic")).grid(row=0,column=0,pady=25, padx=35)
    reportButton=Button(frane,bg='#EEE8AA',text='Record',width=13, font=("Helvetica", 10, "bold italic")).grid(row=0,column=1, pady=25, padx=35)
    b1=Button(frane,text='',bg='#EEE8AA',width=13, font=("Helvetica", 10, "bold italic")).grid(row=0,column=2, pady=25, padx=35)
    b2=Button(frane,text='',bg='#EEE8AA',width=13, font=("Helvetica", 10, "bold italic")).grid(row=0,column=3, pady=25, padx=35)
    global pvtext
    pvtext=Text(frane,width=135,height=20,font=("Helvetica", 10, "bold italic"))
    generateButton=Button(frane,bg='#EEE8AA',text="Generate",width=13, font=("Helvetica", 10, "bold italic"),command=generate).grid(row=5,column=0,pady=25, padx=35)
    pvtext.grid(row=4,column=0,columnspan=4,padx=3, pady=5)
def generate():
    var=pvtext.get('1.0','end-1c')
    with open("pv.txt",'w') as file :
        file.write(var)
    doc = SimpleDocTemplate("PV"+str(time.ctime())+".pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    Story = []
    logo = "bg.gif"
    formatted_time = time.ctime()
    full_name = "G²FOSS COMMUNITY  Record"
    address_parts = ["National school of engineering of tunis ", "G2FOSS CLUB"]
    im = Image(logo, 7 * inch, 2 * inch)
    Story.append(im)
    Story.append(Spacer(1, 40))
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>%s</font>' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>%s</font>' % full_name
    Story.append(Spacer(1, 15))
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 15))
    for part in address_parts:
        ptext = '<font size=12>%s</font>' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 15))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Progress of the general meeting :</font>'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    with open("pv.txt",'r') as file :
        for line in file.readlines() :
            ptext = '<font size=12>%s</font>' % line
            Story.append(Paragraph(ptext, styles["Justify"]))
            Story.append(Spacer(1, 4))

    Story.append(Spacer(1, 40))
    doc.build(Story)
    os.remove('pv.txt')

def Members_Statistics():
    for widget in frane.winfo_children():
        widget.destroy()
    global c,stat,lala,canvaso
    canvaso = Canvas(frane, width=100, height=100, bg='#000000')
    shoButton=Button(frane,bg='#EEE8AA',width=20, font=("Helvetica", 10, "bold italic"),text="Show Statistics",command=ShowStat)
    sesLabel=Label(frane,bg='#EEE8AA',width=20,text="Session Number",font=("Helvetica", 10, "bold italic"))
    global sesEntry

    sesEntry=StringVar()

    sese=Entry(frane,width=20, font=("Helvetica", 10, "bold italic"), textvariable=sesEntry)

    c= StringVar()

    com = ttk.Combobox(frane, width=20, font=("Helvetica", 10, "bold italic"), textvariable=c)
    com.bind("<<ComboboxSelected>>", getimgfdb)
    lala=Label(frane,bg='#EEE8AA',width=20, font=("Helvetica", 10, "bold italic"))
    com['values'] = [i[3] for i in DB.view()]
    canvaso.grid(row=0,column=0,padx=25)
    lala.grid(row=0, column=1, padx=25,pady=25)
    com.grid(row=0,column=2,padx=25)
    shoButton.grid(row=1, column=0, padx=25,pady=25)
    sesLabel.grid(row=1,column=1, padx=25,pady=25)
    sese.grid(row=1,column =2,padx=25,pady=25)
def ShowStat():
    cin=c.get()
    col = DB.cursor.execute("SELECT pr ,att ,par FROM G2FOSSMEMBERS WHERE cin=?", (cin,))
    for row in col:
        pr = int(row[0])
        att = int(row[1])
        par = int(row[2])
    s=int(sesEntry.get())
    prlabels = ["Good", "Bad"]
    values = [pr/s,1-pr/s ]
    actualFigure = plt.figure(figsize=(3.32, 3))
    actualFigure.suptitle("Presence ", fontsize=22)
    explode = list()
    for k in prlabels:
        explode.append(0.1)
    pie, text = plt.pie(values, labels=prlabels, explode=explode, shadow=True)
    canvas = FigureCanvasTkAgg(actualFigure, frane)
    canvas.get_tk_widget().grid(row=2,column=0,rowspan=6)

    atlabels = ["Good", "Bad"]
    values = [att/s,1-att/s ]
    actualFigure = plt.figure(figsize=(3.32, 3))
    actualFigure.suptitle("Attendance", fontsize=22)
    explode = list()
    for k in atlabels:
        explode.append(0.1)
    pie, text = plt.pie(values, labels=atlabels, explode=explode, shadow=True)
    canvas = FigureCanvasTkAgg(actualFigure, frane)
    canvas.get_tk_widget().grid(row=2,column=1,rowspan=6)


    parlabels = ["Good", "Bad"]
    values = [par/s,1-par/s ]
    actualFigure = plt.figure(figsize=(3.32, 3))
    actualFigure.suptitle("Participation", fontsize=22)
    explode = list()
    for k in parlabels:
        explode.append(0.1)
    pie, text = plt.pie(values, labels=parlabels, explode=explode, shadow=False)
    canvas = FigureCanvasTkAgg(actualFigure, frane)
    canvas.get_tk_widget().grid(row=2,column=2,rowspan=6)

def Mails():
    for widget in frane.winfo_children():
        widget.destroy()
    global w1,w2,w3,w4,check1,check2,check3,check4
    w1 = StringVar()
    check1 = ttk.Checkbutton(frane, text='Security Workshop',variable=w1,width=20,onvalue="Security Workshop",offvalue="")
    w2 = StringVar()
    check2 = ttk.Checkbutton(frane, text='Development workshop',variable=w2,width=20,onvalue="Development Workshop",offvalue="")
    w3 = StringVar()
    check3 = ttk.Checkbutton(frane, text='Embeded workshop', variable=w3, width=20, onvalue="Embedded electronics Workshop",
                             offvalue="")
    w4 = StringVar()
    check4 = ttk.Checkbutton(frane, text='All', variable=w4, width=20, onvalue="All",
                             offvalue="")
    l1=Label(frane,bg='#EEE8AA',text="Reception List",width=15,font=("Helvetica", 10, "bold italic"))
    global reclist
    reclist=Listbox(frane, height=6, width=100, font=("Helvetica", 10, "bold italic"))
    s=Scrollbar(frane,orient='vertical', width=20, highlightcolor='red')
    reclist.configure(yscrollcommand=s.set)
    s.configure(command=reclist.yview)
    ShowButton=Button(frane,bg='#EEE8AA', text="Show", width=15, font=("Helvetica", 10, "bold italic"),command=show)
    l2=Label(frane,bg='#EEE8AA',text='Object',width=15,font=("Helvetica", 10, "bold italic"))
    global e2,e1
    e1=Text(frane,width=100,height=3, font=("Helvetica", 10, "bold italic"))
    l3=Label(frane,bg='#EEE8AA',text='content',width=15,font=("Helvetica", 10, "bold italic"))
    e2=Text(frane,width=100,height=8,font=("Helvetica", 10, "bold italic"))
    sendButton=Button(frane,bg='#EEE8AA', text="Send", width=15, font=("Helvetica", 10, "bold italic"),command=send)
    clearButton=Button(frane,bg='#EEE8AA',text='Clear',width=15,font=("Helvetica", 10, "bold italic"),command=clear)
    global attachementPath,comboattachement
    attachementPath=StringVar()
    comboattachement = ttk.Combobox(frane, width=20, font=("Helvetica", 10, "bold italic"), textvariable=attachementPath)
    comboattachement.bind("<<ComboboxSelected>>", getattachement)
    comboattachement['values'] = [i for i in glob.glob("attachement/*")]
    comboattachement.set('attachement/bg.gif')

    check1.grid(row=0,column=0,padx=10, pady=25)
    check2.grid(row=0,column=1,padx=10, pady=25)
    check3.grid(row=0,column=2,padx=10, pady=25)
    check4.grid(row=0,column=3,padx=10, pady=25)
    l1.grid(row=1,column=0,padx=10,pady=25)
    reclist.grid(row=2,column=0,columnspan=4,padx=10,pady=10)
    s.grid(row=2,column=4)
    l2.grid(row=3,column=0,padx=10,pady=25)
    ShowButton.grid(row=3,column=2,padx=10,pady=25)
    e1.grid(row=4,column=0,columnspan=4,padx=3, pady=5)
    l3.grid(row=5,column=0,padx=10,pady=5)
    e2.grid(row=6,column=0,columnspan=4,padx=3, pady=5)
    comboattachement.grid(row=6,column=5,padx=3,pady=5)

    sendButton.grid(row=7,column=0,padx=5, pady=5)
    clearButton.grid(row=7,column=2,padx=5, pady=5)

def getattachement(event):
    global a
    a=str(attachementPath.get())
def clear():
    reclist.delete(0, END)
    e2.delete('1.0', END)
    e1.delete('1.0', END)
    w1.set("")
    w2.set("")
    w3.set("")
    w4.set("")
    comboattachement.set('attachement/bg.gif')




def send():
    for item in reclist.get(0,END):

        email_user = 'pass your email @ here'
        email_password = 'password goes here '
        email_send = item
        subject =e1.get('1.0','end-1c')
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        body = e2.get('1.0','end-1c')
        msg.attach(MIMEText(body, 'plain'))

        filename = a
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, text)
        server.quit()
        messagebox.showinfo("Send ","successfully sent email to %s:" % (msg['To']))

def show():
    reclist.delete(0, END)
    if w4.get()=="All":
        reclist.delete(0, END)
        for row in DB.view():
            reclist.insert(END, row[4])
    elif w1.get()== "Security Workshop":
        reclist.delete(0, END)
        for row in DB.search("","","","","","","","","Security Workshop",""):
            reclist.insert(END, row[4])
    elif w2.get()=="Development Workshop" :
        reclist.delete(0, END)
        for row in DB.search("","","","","","","","" ,"Development Workshop",""):
            reclist.insert(END, row[4])
    elif w3.get()=="Embedded electronics Workshop" :
        reclist.delete(0, END)
        for row in DB.search("","","","","","","","","Embedded electronics Workshop",""):
            reclist.insert(END, row[4])


def Personal_Notations():

    for widget in frane.winfo_children() :
        widget.destroy()
    global n, enot

    n = Listbox(frane, width=60, height=15, font=("Helvetica", 10, "bold italic"))

    enot = Text(frane, width=55, height=15, font=("Helvetica", 10, "bold italic"))

    s1 = Scrollbar(frane, orient='vertical', width=20, highlightcolor='red')
    s2 = Scrollbar(frane, orient='horizontal', width=20, highlightcolor='red')
    n.configure(yscrollcommand=s1.set)
    s1.configure(command=n.yview)
    n.configure(xscrollcommand=s2.set)
    s2.configure(command=n.xview)
    l1 = Label(frane,bg='#EEE8AA', width=60, text="Notations ", font=("Helvetica", 10, "bold italic"))
    l2 = Label(frane, width=55, bg='#EEE8AA',text="Write Notation", font=("Helvetica", 10, "bold italic"))
    checked = Button(frane, bg='#EEE8AA',text="Add Notations", font=("Helvetica", 10, "bold italic"), width=13, command=AddNote)
    shown = Button(frane, text="Show Notations",bg='#EEE8AA', font=("Helvetica", 10, "bold italic"), width=13, command=ShowNot)
    l1.grid(row=0, column=0, pady=25)
    l2.grid(row=0, column=2, pady=25)
    n.grid(row=1, column=0)
    s1.grid(row=1, column=1)
    enot.grid(row=1, column=2)
    shown.grid(row=3,column=0)
    s2.grid(row=2, column=0)
    checked.grid(row=3, column=2, pady=25)
    n.delete(0, END)
def ShowNot() :
    n.delete(0, END)
    con = sqlite3.connect("Notation.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM nota")
    for row in cur.fetchall() :
        n.insert(END, row)
    con.close()


def AddNote():
    con = sqlite3.connect("Notation.db")
    cur = con.cursor()
    cur.execute("INSERT INTO nota  VALUES (NULL,?,?)",(str(datetime.datetime.now()),enot.get('1.0','end-1c')))
    con.commit()
    con.close()
    messagebox.showinfo("NOTATION ","NOTATION ADDED SUCCESSFULLY TO ARCHIVE")


def thirdPage():
    if epassentry.get()!='g2foss':
        messagebox.showinfo("Login Error", "Sorry, try again.")
    else :
        window.configure(bg='#C0C0C0')

        firstFrame.destroy()
        RWidth = window.winfo_screenwidth()
        RHeight = window.winfo_screenheight()
        window.geometry(("%dx%d")%(RWidth, RHeight))
        menu=Menu(window)
        window.config(menu=menu)
        fileMenu = Menu(menu)
        fileMenu.add_separator()
        menu.add_cascade(label="File", menu=fileMenu,font=("Helvetica", 10, "bold italic"))
        menu.add_cascade(label="Save", menu=fileMenu,font=("Helvetica", 10, "bold italic"))
        menu.add_cascade(label="Exit", menu=fileMenu,font=("Helvetica", 10, "bold italic"))
        menu.add_cascade(label="About", menu=fileMenu,font=("Helvetica", 10, "bold italic"))
        frame=Frame(window,bg="#C0C0C0",width=RWidth/5,height=RHeight)
        frame.grid(row=0,column=0)
        a = ImageTk.PhotoImage(file="Free.png")
        global frane
        frane = Frame(window, bg="#C0C0C0", width=RWidth- RWidth / 5, height=RHeight)#3b5998
        frane.grid(row=0, column=1)
        canvasHome = Canvas(frane, width=900, height=500, bg='#000000')
        canvasHome.create_image(0, 0, anchor=NW, image=a)
        canvasHome.image = a
        canvasHome.grid(row=0, column=1,rowspan=10,columnspan=10)
        l=Label(frame,width=35,bg="#C0C0C0")
        global b1 ,anniversaryList
        anniversaryList={}
        i=0
        for val in DB.view() :
            if (int(val[6][0:2])==int(datetime.datetime.now().day )and int(val[6][3:5])==int(datetime.datetime.now().month) ) :
                i+=1
                anniversaryList[val[1:3]]=val[12]

        con = sqlite3.connect("agenda.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM agenda ")
        row = cur.fetchall()
        for event in row:
            if (int(event[1][0:2])-2==int(datetime.datetime.now().day) and int(event[1][3:5])==int(datetime.datetime.now().month)) :
                i+=1
        con.close()

        b1 = Button(frame, text=str(i)+"  "+"Notification", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=Notification)
        b2 = Button(frame, text="Dash Bord", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=Dash)
        b3 = Button(frame, text="Agenda", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=Agenda)
        b4 = Button(frame, text="Send Mails", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=Mails)
        b7 = Button(frame, text="Personal Notations", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=Personal_Notations)
        b6 = Button(frame, text="Inspections", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=Inspections)
        b5 = Button(frame, text="Members Statistics", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=Members_Statistics)
        b8 = Button(frame, text="HRM TOOLS", width=35, font=("Helvetica", 10, "bold italic"),bg='#EEE8AA',command=HRM_TOOLS)
        b1.grid(row=0, column=0, pady=25, padx=10)
        b2.grid(row=1, column=0, pady=25, padx=10)
        b3.grid(row=2, column=0, pady=25, padx=10)
        b4.grid(row=3, column=0, pady=25, padx=10)
        b5.grid(row=4, column=0, pady=25, padx=10)
        b6.grid(row=5, column=0, pady=25, padx=10)
        b7.grid(row=6, column=0, pady=25, padx=10)
        b8.grid(row=7, column=0, pady=25, padx=10)
        l.grid(row=8, column=0, pady=25, padx=10)


def about() :
    path=glob.glob("aboutimg/*.png")
    frames=[ImageTk.PhotoImage(file=i) for i in path]
    global secondFrame
    firstFrame.destroy()
    window.configure(bg='#3b5998')
    secondFrame=Frame(window,bg='#3b5998')
    global bb,fb
    bb=Button(window,text="Back",fg="#FFFFFF",bg="#3b5998",font=("Helvetica", 10, "bold italic"),command=ret)
    fb=Button(window,text="Ping As On FB",bg="#3b5998",fg="#FFFFFF",font=("Helvetica", 10, "bold italic"),
              command=lambda :webbrowser.open("https://web.facebook.com/G2FOSS/",new=1))
    l=Label(secondFrame,text=t,bg="#3b5998",fg="#FFFFFF",font=("Helvetica", 10, "bold italic"))
    canvas = Canvas(secondFrame,width=451, height=300, bg='#3b5998')
    canvas.pack(side='left')
    l.pack(side='right')
    secondFrame.pack()
    for frame in frames :
        canvas.delete(ALL)
        canvas.create_image(0,0,anchor=NW,image=frame)
        canvas.update()
        time.sleep(1.5)

    bureau=ImageTk.PhotoImage(file="aboutimg/33.png")
    canvas.delete(ALL)
    canvas.create_image(0, 0, anchor=NW,image=bureau)
    canvas.image = bureau
    bb.pack(side='left')
    fb.pack(side='right')


def fstPage():
    global firstFrame
    firstFrame = Frame(window)
    firstFrame.configure(bg="#3b5998")

    background_image = PhotoImage(file='bg.gif')

    canavas = Canvas(firstFrame, height=310, width=821)
    canavas.pack()
    canavas.create_image(0, 0, anchor=NW, image=background_image)
    canavas.image=background_image
    global epassentry
    epassentry = StringVar()
    e2 = Entry(firstFrame, show='✪', textvariable=epassentry)
    b1 = Button(firstFrame, text="About As", bg="#3b5998", fg="#FFFFFF",
                font=("Helvetica", 10, "bold italic"),command=about)
    b1.pack(ipadx=821)

    e2.pack(ipadx=200)

    b2 = Button(firstFrame, text="SUDO", bg="#3b5998", fg="#FFFFFF", font=("Helvetica", 10, "bold italic"),command=thirdPage)
    b2.pack(ipadx=821)

    l = Label(firstFrame, text=" <<G²FOSS HRM>>   MADE WITH  <3  FOR  THE G²FOSS COMMUNITY  BY OUERGHI FIRAS ",bg="#3b5998", fg="#FFFFFF", font=("Helvetica", 10, "bold italic"))

    l.pack(ipadx=821, ipady=1)
    firstFrame.pack()

def main():
    global window
    window=Tk()
    #the code goes here
    window.geometry("820x420")
    window.title("~HRM~G²FOSS~")
    window.configure(bg="#C0C0C0")
    fstPage()

    window.mainloop()


if __name__=="__main__" :
    main()
