from tkinter import *
import mysql.connector
from mysql import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


import mysql.connector as sql
connection=sql.connect(host='localhost',user='root',password="Teracome123@?",auth_plugin='mysql_native_password')
mycursor=connection.cursor()
mycursor.execute("create database stock")

def db():
    root = Tk()
    root.title("Stock List")
    width = 700
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    root.config(bg="#6666ff")

    #============================VARIABLES===================================
    NAME = StringVar()
    CATEGERY = StringVar()
    PRICE = StringVar()
    UNITS = StringVar()
    ADDRESS = StringVar()
    CONTACT = StringVar()



    #============================METHODS=====================================

    def Database():
        conn = mysql.connector.connect(host='localhost',user='root',password='Teracome123@?',database='stock')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS stock (mem_id INTEGER NOT NULL  PRIMARY KEY AUTO_INCREMENT,name varchar(20), categery varchar(20), price varchar(20), unit varchar(20), address varchar(20),contact varchar(20))")
        cursor.execute("SELECT * FROM stock ORDER BY name")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def SubmitData():
        if  NAME.get() == "" or CATEGERY.get() == "" or PRICE.get() == "" or UNITS.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
            result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
            conn = mysql.connector.connect(host='localhost',user='root',password='Teracome123@?',database='stock')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO stock (name, categery, price, unit, address, contact) VALUES(%s, %s, %s, %s, %s, %s)", (str(NAME.get()), str(CATEGERY.get()), str(PRICE.get()), str(UNITS.get()), str(ADDRESS.get()), str(CONTACT.get())))
            conn.commit()
            cursor.execute("SELECT * FROM stock ORDER BY name")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
            NAME.set("")
            CATEGERY.set("")
            PRICE.set("")
            UNITS.set("")
            ADDRESS.set("")
            CONTACT.set("")

    def UpdateData():
        if  NAME.get() == "" or CATEGERY.get() == "" or PRICE.get() == "" or UNITS.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
           result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
            conn = mysql.connector.connect(host='localhost',user='root',password='Teracome123@?',database='stock')
            cursor = conn.cursor()
            cursor.execute("UPDATE stock SET name = %s, categery = %s, price =%s, unit = %s,  address = %s, contact = %s WHERE mem_id = %s", (str(NAME.get()), str(CATEGERY.get()), str(PRICE.get()), str(UNITS.get()), str(ADDRESS.get()), str(CONTACT.get()), int(mem_id)))
            conn.commit()
            cursor.execute("SELECT * FROM STOCK ORDER BY name")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            UpdateWindow.destroy()
            
    def OnSelected(event):
        global mem_id, UpdateWindow
        curItem = tree.focus()
        contents =(tree.item(curItem))
        selecteditem = contents['values']
        mem_id = selecteditem[0]
        NAME.set("")
        CATEGERY.set("")
        PRICE.set("")
        UNITS.set("")
        ADDRESS.set("")
        CONTACT.set("")
        NAME.set(selecteditem[1])
        CATEGERY.set(selecteditem[2])
        PRICE.set(selecteditem[3])
        UNITS.set(selecteditem[4])
        ADDRESS.set(selecteditem[5])
        CONTACT.set(selecteditem[6])
        UpdateWindow = Toplevel()
        UpdateWindow.title("stock details")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) + 450) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        UpdateWindow.resizable(0, 0)
        UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        if 'NewWindow' in globals():
            NewWindow.destroy()

        #===================FRAMES==============================
        FormTitle = Frame(UpdateWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(UpdateWindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
                #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Updating details", font=('arial', 16), bg="orange",  width = 300)
        lbl_title.pack(fill=X)
        lbl_name = Label(ContactForm, text="NAME", font=('arial', 14), bd=5)
        lbl_name.grid(row=0, sticky=W)
        lbl_CAT = Label(ContactForm, text="CATEGORY", font=('arial', 14), bd=5)
        lbl_CAT.grid(row=1, sticky=W)
        lbl_price = Label(ContactForm, text="PRICE", font=('arial', 14), bd=5)
        lbl_price.grid(row=2, sticky=W)
        lbl_units = Label(ContactForm, text="Units", font=('arial', 14), bd=5)
        lbl_units.grid(row=3, sticky=W)
        lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
        lbl_address.grid(row=4, sticky=W)
        lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
        lbl_contact.grid(row=5, sticky=W)

        #===================ENTRY===============================
        name = Entry(ContactForm, textvariable=NAME, font=('arial', 14))
        name.grid(row=0, column=1)
        CAT = Entry(ContactForm, textvariable=CATEGERY, font=('arial', 14))
        CAT.grid(row=1, column=1)
        price = Entry(ContactForm, textvariable=PRICE, font=('arial', 14))
        price.grid(row=2, column=1)
        units = Entry(ContactForm, textvariable=UNITS,  font=('arial', 14))
        units.grid(row=3, column=1)
        address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
        address.grid(row=4, column=1)
        contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
        contact.grid(row=5, column=1)
        price = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
        price.grid(row=5, column=1)

        #==================BUTTONS==============================
        btn_updatecon = Button(ContactForm, text="Update",bd=10, width=50, command=UpdateData)
        btn_updatecon.grid(row=6, columnspan=2, pady=10)


    #fn1353p    
    def DeleteData():
        if not tree.selection():
           result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
        else:
            result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents =(tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                conn = mysql.connector.connect(host='localhost',user='root',password='123',database='stock')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM STOCK WHERE mem_id = %d" % selecteditem[0])
                conn.commit()
                cursor.close()
                conn.close()
        
    def AddNewWindow():
        global NewWindow
        NAME.set("")
        CATEGERY.set("")
        PRICE.set("")
        UNITS.set("")
        ADDRESS.set("")
        CONTACT.set("")
        NewWindow = Toplevel()
        NewWindow.title("Contact List")
        width = 400
        height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = ((screen_width/2) - 455) - (width/2)
        y = ((screen_height/2) + 20) - (height/2)
        NewWindow.resizable(0, 0)
        NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()
        
        #===================FRAMES==============================
        FormTitle = Frame(NewWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(NewWindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        
        
        #===================LABELS==============================
        lbl_title = Label(FormTitle, text="Adding stock details", font=('arial', 16), bg="#66ff66",  width = 300)
        lbl_title.pack(fill=X)
        lbl_firstname = Label(ContactForm, text="name", font=('arial', 14), bd=5)
        lbl_firstname.grid(row=0, sticky=W)
        lbl_lastname = Label(ContactForm, text="categery", font=('arial', 14), bd=5)
        lbl_lastname.grid(row=1, sticky=W)
        lbl_gender = Label(ContactForm, text="price", font=('arial', 14), bd=5)
        lbl_gender.grid(row=2, sticky=W)
        lbl_age = Label(ContactForm, text="units", font=('arial', 14), bd=5)
        lbl_age.grid(row=3, sticky=W)
        lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
        lbl_address.grid(row=4, sticky=W)
        lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
        lbl_contact.grid(row=5, sticky=W)

        #===================ENTRY===============================
        firstname = Entry(ContactForm, textvariable=NAME, font=('arial', 14))
        firstname.grid(row=0, column=1)
        lastname = Entry(ContactForm, textvariable=CATEGERY, font=('arial', 14))
        lastname.grid(row=1, column=1)
        gender = Entry(ContactForm, textvariable=PRICE, font=('arial', 14))
        gender.grid(row=2, column=1)
        age = Entry(ContactForm, textvariable=UNITS,  font=('arial', 14))
        age.grid(row=3, column=1)
        address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
        address.grid(row=4, column=1)
        contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
        contact.grid(row=5, column=1)
        

        #==================BUTTONS==============================
        btn_addcon = Button(ContactForm, text="Save",bd=10, width=50, command=SubmitData)
        btn_addcon.grid(row=6, columnspan=2, pady=10)




        
    #============================FRAMES======================================
    Top = Frame(root, width=500, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    Mid = Frame(root, width=500,  bg="#6666ff")
    Mid.pack(side=TOP)
    MidLeft = Frame(Mid, width=100)
    MidLeft.pack(side=LEFT, pady=10)
    MidLeftPadding = Frame(Mid, width=370, bg="#6666ff")
    MidLeftPadding.pack(side=LEFT)
    MidRight = Frame(Mid, width=100)
    MidRight.pack(side=RIGHT, pady=10)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    #============================LABELS======================================
    lbl_title = Label(Top, text="Stock management system", font=('arial', 16), width=500)
    lbl_title.pack(fill=X)

    #============================ENTRY=======================================

    #============================BUTTONS=====================================
    btn_add = Button(MidLeft, text="+ ADD NEW", bd=10,bg="#66ff66", command=AddNewWindow)
    btn_add.pack()
    btn_delete = Button(MidRight, text="DELETE",bd=10, bg="red", command=DeleteData)
    btn_delete.pack(side=RIGHT)

    #============================TABLES======================================
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("MemberID", "name", "Categery", "Price", "Units", "Address", "Contact"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('MemberID', text="MemberID", anchor=W)
    tree.heading('name', text="name", anchor=W)
    tree.heading('Categery', text="Categery", anchor=W)
    tree.heading('Price', text="Price", anchor=W)
    tree.heading('Units', text="Units", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)
    tree.pack()
    tree.bind('<Double-Button-1>', OnSelected)

    #============================INITIALIZATION==============================

    Database()
    root.mainloop()
        




