from tkinter import *
from tkinter import ttk #for combox gender
from tkinter import messagebox
from db import database

db1=database("employee.db")

win =Tk()
win.title("data entry")
win.geometry("1366x768+0+0")
win.configure(bg="#2274A5")
win.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()
address=StringVar()

#entries frame
entries_f = Frame(win,bg="#A33B20")
entries_f.pack(side=TOP,fill=X)
title=Label(entries_f,text="data entry",font=("calibri",20,"bold"),bg="#A33B20",fg="white")
title.grid(row=0,columnspan=2)

lname = Label(entries_f,text="Name",font=("calibri",20),bg="#A33B20",fg="white")
lname.grid(row=1,column=0,padx=10,pady=10,sticky="w")
nentry=Entry(entries_f,textvariable=name,font=("calibri",20),width=30)
nentry.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lage = Label(entries_f,text="Age",font=("calibri",20),bg="#A33B20",fg="white")
lage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
aentry=Entry(entries_f,textvariable=age,font=("calibri",20),width=30)
aentry.grid(row=1,column=3,padx=10,pady=10,sticky="w")

ldoj = Label(entries_f,text="DOJ",font=("calibri",20),bg="#A33B20",fg="white")
ldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
dentry=Entry(entries_f,textvariable=doj,font=("calibri",20),width=30)
dentry.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lemail = Label(entries_f,text="Email",font=("calibri",20),bg="#A33B20",fg="white")
lemail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
eentry=Entry(entries_f,textvariable=email,font=("calibri",20),width=30)
eentry.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lgender = Label(entries_f,text="Gender",font=("calibri",20),bg="#A33B20",fg="white")
lgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
gentry=ttk.Combobox(entries_f,textvariable=gender,font=("calibri",20),state="readonly",width=30)
gentry['values']=("male","female")
gentry.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lcontact = Label(entries_f,text="Contact",font=("calibri",20),bg="#A33B20",fg="white")
lcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
conentry=Entry(entries_f,textvariable=contact,font=("calibri",20),width=30)
conentry.grid(row=3,column=3,padx=10,pady=10,sticky="w")

laddress = Label(entries_f,text="Address",font=("calibri",20),bg="#A33B20",fg="white")
laddress.grid(row=4,column=0,padx=10,sticky="w")

addentry=Text(entries_f,font=("calibri",20),width=80,height=3)
addentry.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getdata(event):
    select_row = table.focus()
    data=table.item(select_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    addentry.delete(1.0,END)
    addentry.insert(END,row[7])


def displayall():
    table.delete(*table.get_children())
    for i in db1.fetch():
        table.insert("",END,values=i)

def add_employee():
    if nentry.get()=="" or aentry.get()=="" or dentry.get()=="" or eentry.get()=="" or gentry.get()=="" or conentry.get()=="" or addentry.get(1.0,END)=="":
        messagebox.showerror("Erorr in Input","fill all colums")
        return
    db1.insert(nentry.get(),aentry.get(),dentry.get(),eentry.get(),gentry.get(),conentry.get(),addentry.get(1.0,END))
    clearall()
    displayall()
    messagebox.showinfo("success1", "added successfully")


def update_employee():
    if nentry.get() == "" or aentry.get() == "" or dentry.get() == "" or eentry.get() == "" or gentry.get() == "" or conentry.get() == "" or addentry.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "fill all colums")
        return
    db1.update(row[0],nentry.get(), aentry.get(), dentry.get(), eentry.get(), gentry.get(), conentry.get(),
               addentry.get(1.0, END))
    clearall()
    displayall()
    messagebox.showinfo("success1", "update successfully")

def delete_employee():
    db1.remove(row[0])
    clearall()
    displayall()
    messagebox.showinfo("delete","deleted")

def clearall():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")

    addentry.delete(1.0,END)

btn_frame=Frame(entries_f,bg="#A33B20")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

btnadd=Button(btn_frame,command=add_employee,text="add details",width=15,font=("calibri",20,"bold"),fg="white",bg="#264653",bd=0)
btnadd.grid(row=0,column=0,padx=10)

btnupdate=Button(btn_frame,command=update_employee,text="update",width=15,font=("calibri",20,"bold"),fg="white",bg="#1B263B",bd=0)
btnupdate.grid(row=0,column=1,padx=10)

btndelete=Button(btn_frame,command=delete_employee,text="delete",width=15,font=("calibri",20,"bold"),fg="white",bg="#E76F51",bd=0)
btndelete.grid(row=0,column=2,padx=10)

btnclear=Button(btn_frame,command=clearall,text="clear all",width=15,font=("calibri",20,"bold"),fg="white",bg="#D62828",bd=0)
btnclear.grid(row=0,column=3,padx=10)

#table frame
tree_frame=Frame(win,bg="#BBD0FF")
tree_frame.place(x=0,y=430,width=1420,height=400)

style=ttk.Style()
style.configure("style1.Treeview",font=('Calibri',18),rowheight=50) #modify the font of table
style.configure("style1.Treeview.Heading",font=('Calibri',20)) #modify the font of heading of table

table = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="style1.Treeview")
table.heading("1",text="ID")
table.column("1",width=5)
table.heading("2",text="Name")
table.column("2",width=30)
table.heading("3",text="Age")
table.column("3",width=5)
table.heading("4",text="D.O.J")
table.column("4",width=10)
table.heading("5",text="Email")
table.heading("6",text="Gender")
table.column("6",width=15)
table.heading("7",text="Contact")
table.column("7",width=20)
table.heading("8",text="Address")
table['show']='headings'
table.bind("<ButtonRelease-1>",getdata)
table.pack(fill=X)

displayall()
win.mainloop()
