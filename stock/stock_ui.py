from tkinter import*
import tkinter.messagebox as tkMessageBox
import random
import time
import db
def stocklog():
    def Ref():
        username=str(user.get())
        pas=str(password.get())
        if username=="root" and pas=='123456':
            db.db()
        else:
            result = tkMessageBox.showwarning('', 'Incorrect User or password please try again', icon="warning")
    root = Tk()
    root.geometry("420x360+0+0")
    root.title("SIMPLE CAFE BILLING SYSTEM")

    Tops = Frame(root,width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)

    f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
    f2.pack(side=RIGHT)
    #------------------TIME--------------
    localtime=time.asctime(time.localtime(time.time()))
    #-----------------INFO TOP------------

    user = StringVar()
    password=StringVar()

    ################################################input boxes##################################################
    lblinfo = Label(Tops, font=( 'algerian' ,30, 'bold' ),text="stock database",fg="Black",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    lblinfo = Label(Tops, font=( 'arial' ,20, ),text=localtime,fg="black",anchor=W)
    lblinfo.grid(row=1,column=0)

    lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="User",fg="black",bd=10,anchor='w')
    lblDrinks.grid(row=1,column=2)
    txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=user , bd=6,insertwidth=4,bg="white" ,justify='center')
    txtDrinks.grid(row=1,column=3)

    lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="password",fg="black",bd=10,anchor='w')
    lblburger.grid(row=4,column=2)
    txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=password , bd=6,insertwidth=4,bg="white" ,justify='center')
    txtburger.grid(row=4,column=3)
    ################################buttons##############################################################

    btnlogin=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="login", bg="white",command=Ref)
    btnlogin.grid(row=8, column=3)
stocklog()
