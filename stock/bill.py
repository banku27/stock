from tkinter import *
import time
import datetime
import random

import tkinter.messagebox as tkMessageBox
root =Tk()
root.geometry("1350x750+0+0")
root.title("WHOLE SALE SHOP BILLING SYSTEM")
root.configure(background='orange')

Tops = Frame(root,bg='orange',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',30,'bold'),text='WHOLE SALE SHOP BILLING SYSTEM',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='orange',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='orange',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='orange',bd=5,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='orange',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='orange',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='orange',bd=4)
Cost_F.pack(side=BOTTOM)
External_F=Frame(MenuFrame,bg='orange',bd=4)
External_F.pack(side=TOP)


External_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
External_F.pack(side=LEFT)
Edibles_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
Edibles_F.pack(side=RIGHT)
###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofExternal = StringVar()
CostofEdibles = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Soap = StringVar()
E_Toothpaste = StringVar()
E_Lizol = StringVar()
E_Shampoo = StringVar()
E_Harpic = StringVar()
E_Detergentcake = StringVar()
E_Detergentpowder = StringVar()
E_Conditioner = StringVar()

E_Chocolate = StringVar()
E_Tomatoketchup = StringVar()
E_Pasta = StringVar()
E_Bread = StringVar()
E_Biscuits = StringVar()
E_Chips = StringVar()
E_Bakingpowder = StringVar()
E_Milkpacket = StringVar()

E_Soap.set("0")
E_Toothpaste.set("0")
E_Lizol.set("0")
E_Shampoo.set("0")
E_Harpic.set("0")
E_Detergentcake.set("0")
E_Detergentpowder.set("0")
E_Conditioner.set("0")

E_Chocolate.set("0")
E_Tomatoketchup.set("0")
E_Pasta.set("0")
E_Bread.set("0")
E_Biscuits.set("0")
E_Chips.set("0")
E_Bakingpowder.set("0")
E_Milkpacket.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkMessageBox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofExternal.set("")
    CostofEdibles.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Soap.set("0")
    E_Toothpaste.set("0")
    E_Lizol.set("0")
    E_Shampoo.set("0")
    E_Harpic.set("0")
    E_Detergentcake.set("0")
    E_Detergentpowder.set("0")
    E_Conditioner.set("0")

    E_Chocolate.set("0")
    E_Tomatoketchup.set("0")
    E_Pasta.set("0")
    E_Bread.set("0")
    E_Biscuits.set("0")
    E_Chips.set("0")
    E_Bakingpowder.set("0")
    E_Milkpacket.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtSoap.configure(state=DISABLED)
    txtToothpaste.configure(state=DISABLED)
    txtLizol.configure(state=DISABLED)
    txtShampoo.configure(state=DISABLED)
    txtHarpic.configure(state=DISABLED)
    txtDetergentcake.configure(state=DISABLED)
    txtDetergentpowder.configure(state=DISABLED)
    txtConditioner.configure(state=DISABLED)
    txtChocolate.configure(state=DISABLED)
    txtTomatoketchup.configure(state=DISABLED)
    txtPasta.configure(state=DISABLED)
    txtBread.configure(state=DISABLED)
    txtBiscuits.configure(state=DISABLED)
    txtChips.configure(state=DISABLED)
    txtBakingpowder.configure(state=DISABLED)
    txtMilkpacket.configure(state=DISABLED)

def CostofItem():
    if (E_Soap.get()!="0"  and E_Soap.get()!="") or (E_Toothpaste.get()!="0" and E_Toothpaste.get()!="") or (E_Lizol.get()!="0" and E_Lizol.get()!="0") or (E_Shampoo.get()!="0" and E_Shampoo.get()!="") or (E_Harpic.get()!='0' and E_Harpic.get()!='') or (E_Detergentcake.get()!='0' and E_Detergentcake.get()!='') or (E_Detergentpowder.get()!='0' and  E_Detergentpowder.get()!='') or (E_Conditioner.get()!='0' and E_Conditioner.get()!='0') or (E_Chocolate.get() != '0' and E_Chocolate.get() != '') or (E_Tomatoketchup.get() != '0' and E_Tomatoketchup.get() != '') or (E_Pasta.get()!='0' and E_Pasta.get()!='') or (E_Bread.get() !='0' and E_Bread.get() !='0')or (E_Biscuits.get() != '0' and E_Biscuits.get() != '') or (E_Chips.get() != '0' and E_Chips.get() != '') or (E_Bakingpowder.get() != '0' and E_Bakingpowder.get() != '') or (E_Milkpacket.get() != '0' and E_Milkpacket.get() != ''):
        Item1=float(E_Soap.get())
        Item2=float(E_Toothpaste.get())
        Item3=float(E_Lizol.get())
        Item4=float(E_Shampoo.get())
        Item5=float(E_Harpic.get())
        Item6=float(E_Detergentcake.get())
        Item7=float(E_Detergentpowder.get())
        Item8=float(E_Conditioner.get())

        Item9=float(E_Chocolate.get())
        Item10=float(E_Tomatoketchup.get())
        Item11=float(E_Pasta.get())
        Item12=float(E_Bread.get())
        Item13=float(E_Biscuits.get())
        Item14=float(E_Chips.get())
        Item15=float(E_Bakingpowder.get())
        Item16=float(E_Milkpacket.get())

        PriceofExternal =(Item1 * 800) + (Item2 * 1200) + (Item3 *1100 ) + (Item4 * 2700) + (Item5 * 1500) + (Item6 * 1000) + (Item7 * 1800) + (Item8 * 6000)

        PriceofEdibles =(Item9 * 9000) + (Item10 * 1300) + (Item11 * 400) + (Item12 * 1000) + (Item13 * 900) + (Item14 * 900) + (Item15 * 1400) + (Item16 * 1500)



        ExternalPrice = "Rs",str('%.2f'%(PriceofExternal))
        EdiblesPrice =  "Rs",str('%.2f'%(PriceofEdibles))
        CostofEdibles.set(EdiblesPrice)
        CostofExternal.set(ExternalPrice)
        SC = "Rs",str('%.2f'%(150))
        ServiceCharge.set(SC)

        SubTotalofITEMS = "Rs",str('%.2f'%(PriceofExternal + PriceofEdibles + 150))
        SubTotal.set(SubTotalofITEMS)

        Tax = "Rs",str('%.2f'%((PriceofExternal + PriceofEdibles + 150) * 0.25))
        PaidTax.set(Tax)

        TT=((PriceofExternal + PriceofEdibles + 150) * 0.25)
        TC="Rs",str('%.2f'%(PriceofExternal + PriceofEdibles + 150 + TT))
        TotalCost.set(TC)
    else:
        result = tkMessageBox.showwarning('', 'Please select anyone product', icon="warning")

def chk_Soap():
    if(var1.get() == 1):
        txtSoap.configure(state = NORMAL)
        txtSoap.focus()
        txtSoap.delete('0',END)
        E_Soap.set("")
    elif(var1.get() == 0):
        txtSoap.configure(state = DISABLED)
        E_Soap.set("0")

def chk_Toothpaste():
    if(var2.get() == 1):
        txtToothpaste.configure(state = NORMAL)
        txtToothpaste.focus()
        txtToothpaste.delete('0',END)
        E_Toothpaste.set("")
    elif(var2.get() == 0):
        txtToothpaste.configure(state = DISABLED)
        E_Toothpaste.set("0")

def chk_Lizol():
    if(var3.get() == 1):
        txtLizol.configure(state = NORMAL)
        txtLizol.delete('0',END)
        txtLizol.focus()
    elif(var3.get() == 0):
        txtLizol.configure(state = DISABLED)
        E_Lizol.set("0")

def chk_Shampoo():
    if(var4.get() == 1):
        txtShampoo.configure(state = NORMAL)
        txtShampoo.delete('0',END)
        txtShampoo.focus()
    elif(var4.get() == 0):
        txtShampoo.configure(state = DISABLED)
        E_Shampoo.set("0")

def chk_Harpic():
    if(var5.get() == 1):
        txtHarpic.configure(state = NORMAL)
        txtHarpic.delete('0',END)
        txtHarpic.focus()
    elif(var5.get() == 0):
        txtHarpic.configure(state = DISABLED)
        E_Harpic.set("0")

def chk_Detergentcake():
    if(var6.get() == 1):
        txtDetergentcake.configure(state = NORMAL)
        txtDetergentcake.delete('0',END)
        txtDetergentcake.focus()
    elif(var6.get() == 0):
        txtDetergentcake.configure(state = DISABLED)
        E_Detergentcake.set("0")

def chk_Detergentpowder():
    if(var7.get() == 1):
        txtDetergentpowder.configure(state = NORMAL)
        txtDetergentpowder.delete('0',END)
        txtDetergentpowder.focus()
    elif(var7.get() == 0):
        txtDetergentpowder.configure(state = DISABLED)
        E_Detergentpowder.set("0")

def chk_Conditioner():
    if(var8.get() == 1):
        txtConditioner.configure(state = NORMAL)
        txtConditioner.delete('0',END)
        txtConditioner.focus()
    elif(var8.get() == 0):
        txtConditioner.configure(state = DISABLED)
        E_Conditioner.set("0")

def chk_Chocolate():
    if(var9.get() == 1):
        txtChocolate.configure(state = NORMAL)
        txtChocolate.delete('0',END)
        txtChocolate.focus()
    elif(var9.get() == 0):
        txtChocolate.configure(state = DISABLED)
        E_Chocolate.set("0")

def chk_Tomatoketchup():
    if(var10.get() == 1):
        txtTomatoketchup.configure(state = NORMAL)
        txtTomatoketchup.delete('0',END)
        txtTomatoketchup.focus()
    elif(var10.get() == 0):
        txtTomatoketchup.configure(state = DISABLED)
        E_Tomatoketchup.set("0")

def chk_Pasta():
    if(var11.get() == 1):
        txtPasta.configure(state = NORMAL)
        txtPasta.delete('0',END)
        txtPasta.focus()
    elif(var11.get() == 0):
        txtPasta.configure(state = DISABLED)
        E_Pasta.set("0")

def chk_Bread():
    if(var12.get() == 1):
        txtBread.configure(state = NORMAL)
        txtBread.delete('0',END)
        txtBread.focus()
    elif(var12.get() == 0):
        txtBread.configure(state = DISABLED)
        E_Bread.set("0")

def chk_Biscuits():
    if(var13.get() == 1):
        txtBiscuits.configure(state = NORMAL)
        txtBiscuits.delete('0',END)
        txtBiscuits.focus()
    elif(var13.get() == 0):
        txtBiscuits.configure(state = DISABLED)
        E_Biscuits.set("0")

def chk_Chips():
    if(var14.get() == 1):
        txtChips.configure(state = NORMAL)
        txtChips.delete('0',END)
        txtChips.focus()
    elif(var14.get() == 0):
        txtChips.configure(state = DISABLED)
        E_Chips.set("0")

def chk_Bakingpowder():
    if(var15.get() == 1):
        txtBakingpowder.configure(state = NORMAL)
        txtBakingpowder.delete('0',END)
        txtBakingpowder.focus()
    elif(var15.get() == 0):
        txtBakingpowder.configure(state = DISABLED)
        E_Bakingpowder.set("0")

def chk_Milkpacket():
    if(var16.get() == 1):
        txtMilkpacket.configure(state = NORMAL)
        txtMilkpacket.delete('0',END)
        txtMilkpacket.focus()
    elif(var16.get() == 0):
        txtMilkpacket.configure(state = DISABLED)
        E_Milkpacket.set("0")

def Receipt():
    if (E_Soap.get()!="0"  and E_Soap.get()!="") or (E_Toothpaste.get()!="0" and E_Toothpaste.get()!="") or (E_Lizol.get()!="0" and E_Lizol.get()!="0") or (E_Shampoo.get()!="0" and E_Shampoo.get()!="") or (E_Harpic.get()!='0' and E_Harpic.get()!='') or (E_Detergentcake.get()!='0' and E_Detergentcake.get()!='') or (E_Detergentpowder.get()!='0' and  E_Detergentpowder.get()!='') or (E_Conditioner.get()!='0' and E_Conditioner.get()!='0') or (E_Chocolate.get() != '0' and E_Chocolate.get() != '') or (E_Tomatoketchup.get() != '0' and E_Tomatoketchup.get() != '') or (E_Pasta.get()!='0' and E_Pasta.get()!='') or (E_Bread.get() !='0' and E_Bread.get() !='0')or (E_Biscuits.get() != '0' and E_Biscuits.get() != '') or (E_Chips.get() != '0' and E_Chips.get() != '') or (E_Bakingpowder.get() != '0' and E_Bakingpowder.get() != '') or (E_Milkpacket.get() != '0' and E_Milkpacket.get() != ''):
        txtReceipt.delete("1.0",END)
        x=random.randint(10908,500876)
        randomRef= str(x)
        Receipt_Ref.set("Bill"+ randomRef)


        txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
        txtReceipt.insert(END,'Items\t\t\t\t'+"no. of Items \n")
        txtReceipt.insert(END,'Soap:\t\t\t\t\t' + E_Soap.get() +'\n')
        txtReceipt.insert(END,'Toothpaste:\t\t\t\t\t'+ E_Toothpaste.get()+'\n')
        txtReceipt.insert(END,'Lizol:\t\t\t\t\t'+ E_Lizol.get()+'\n')
        txtReceipt.insert(END,'Shampoo:\t\t\t\t\t'+ E_Shampoo.get()+'\n')
        txtReceipt.insert(END,'Harpic:\t\t\t\t\t'+ E_Harpic.get()+'\n')
        txtReceipt.insert(END,'Detergent cake:\t\t\t\t\t'+ E_Detergentcake.get()+'\n')
        txtReceipt.insert(END,'Detergent powder:\t\t\t\t\t'+ E_Detergentpowder.get()+'\n')
        txtReceipt.insert(END,'Conditioner:\t\t\t\t\t'+ E_Conditioner.get()+'\n')
        txtReceipt.insert(END,'Chocolate:\t\t\t\t\t'+ E_Chocolate.get()+'\n')
        txtReceipt.insert(END,'Tomato ketchup:\t\t\t\t\t'+ E_Tomatoketchup.get()+'\n')
        txtReceipt.insert(END,'Pasta:\t\t\t\t\t'+ E_Pasta.get()+'\n')
        txtReceipt.insert(END,'Bread:\t\t\t\t\t'+ E_Bread.get()+'\n')
        txtReceipt.insert(END,'Biscuits:\t\t\t\t\t'+ E_Biscuits.get()+'\n')
        txtReceipt.insert(END,'Chips:\t\t\t\t\t'+ E_Chips.get()+'\n')
        txtReceipt.insert(END,'Baking powder:\t\t\t\t\t'+ E_Bakingpowder.get()+'\n')
        txtReceipt.insert(END,'Milk packet:\t\t\t\t\t'+ E_Milkpacket.get()+'\n')
        txtReceipt.insert(END,'Cost of External:\t\t\t\t'+ CostofExternal.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
        txtReceipt.insert(END,'Cost of Edibles:\t\t\t\t'+ CostofEdibles.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
        txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")
    else:
        result = tkMessageBox.showwarning('', 'Please select anyone product', icon="warning")

#########################################External####################################################################
Soap=Checkbutton(External_F,text='Soap(30pcs,Rs.800)',variable=var1,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                    bg='orange',command=chk_Soap).grid(row=0,sticky=W)
Toothpaste=Checkbutton(External_F,text='Toothpaste(50pcs,Rs.1200)',variable=var2,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                    bg='orange',command=chk_Toothpaste).grid(row=1,sticky=W)
Lizol=Checkbutton(External_F,text='Lizol(20pcs,Rs.1100)',variable=var3,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                    bg='orange',command=chk_Lizol).grid(row=2,sticky=W)
Shampoo=Checkbutton(External_F,text='Shampoo(30pcs,Rs.2700)',variable=var4,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                    bg='orange',command=chk_Shampoo).grid(row=3,sticky=W)
Harpic=Checkbutton(External_F,text='Harpic(30pcs,RS.1500)',variable=var5,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                   bg='orange',command=chk_Harpic).grid(row=4,sticky=W)
Detergentcake=Checkbutton(External_F,text='Detergent cake(30pcs,Rs.1000)',variable=var6,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                    bg='orange',command=chk_Detergentcake).grid(row=5,sticky=W)
Detergentpowder=Checkbutton(External_F,text='Detergent powder(30pcs,Rs.1800)',variable=var7,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                    bg='orange',command=chk_Detergentpowder).grid(row=6,sticky=W)
Conditioner=Checkbutton(External_F,text='Conditioner(30pcs,Rs.6000)',variable=var8,onvalue=1,offvalue=0,font=('arial',14,'bold'),
                    bg='orange',command=chk_Conditioner).grid(row=7,sticky=W)
##############################################External###############################################################

txtSoap= Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Soap)
txtSoap.grid(row=0,column=1)

txtToothpaste = Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Toothpaste)
txtToothpaste.grid(row=1,column=1)

txtLizol = Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Lizol)
txtLizol.grid(row=2,column=1)

txtShampoo= Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Shampoo)
txtShampoo.grid(row=3,column=1)

txtHarpic = Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Harpic)
txtHarpic.grid(row=4,column=1)

txtDetergentcake = Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Detergentcake)
txtDetergentcake.grid(row=5,column=1)

txtDetergentpowder = Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Detergentpowder)
txtDetergentpowder.grid(row=6,column=1)

txtConditioner = Entry(External_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Conditioner)
txtConditioner.grid(row=7,column=1)
#############################################Foods######################################################################

Chocolate = Checkbutton(Edibles_F,text="Chocolate(100pcs,Rs.9000) ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Chocolate).grid(row=0,sticky=W)
Tomatoketchup = Checkbutton(Edibles_F,text="Tomatoketchup(40pcs,Rs.1300)",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Tomatoketchup).grid(row=1,sticky=W)
Pasta = Checkbutton(Edibles_F,text="Pasta(30pcs,Rs.400) ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Pasta).grid(row=2,sticky=W)
Bread = Checkbutton(Edibles_F,text="Bread(30pcs,Rs.1000) ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Bread).grid(row=3,sticky=W)
Biscuits = Checkbutton(Edibles_F,text="Biscuits(100pcs,Rs.900) ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Biscuits).grid(row=4,sticky=W)
Chips = Checkbutton(Edibles_F,text="Chips(100pcs,Rs.900) ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Chips).grid(row=5,sticky=W)
Bakingpowder = Checkbutton(Edibles_F,text="Bakingpowder(30pcs,Rs.1400) ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Bakingpowder).grid(row=6,sticky=W)
Milkpacket = Checkbutton(Edibles_F,text="Milk packet(40pcs,Rs.1500) ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',14,'bold'),bg='orange',command=chk_Milkpacket).grid(row=7,sticky=W)
################################################Entry Box For Cake##########################################################
txtChocolate=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Chocolate)
txtChocolate.grid(row=0,column=1)

txtTomatoketchup=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Tomatoketchup)
txtTomatoketchup.grid(row=1,column=1)

txtPasta=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Pasta)
txtPasta.grid(row=2,column=1)

txtBread=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Bread)
txtBread.grid(row=3,column=1)

txtBiscuits=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Biscuits)
txtBiscuits.grid(row=4,column=1)

txtChips=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Chips)
txtChips.grid(row=5,column=1)

txtBakingpowder=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Bakingpowder)
txtBakingpowder.grid(row=6,column=1)

txtMilkpacket=Entry(Edibles_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Milkpacket)
txtMilkpacket.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofExternal=Label(Cost_F,font=('arial',14,'bold'),text='Cost of External',bg='orange',
                fg='black',justify=CENTER)
lblCostofExternal.grid(row=0,column=0,sticky=W)
txtCostofExternal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofExternal)
txtCostofExternal.grid(row=0,column=1)

lblCostofEdibles=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Edibles  ',bg='orange',
                fg='black',justify=CENTER)
lblCostofEdibles.grid(row=1,column=0,sticky=W)
txtCostofEdibles=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofEdibles)
txtCostofEdibles.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='orange',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='orange',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='orange',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='orange',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='orange',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='orange',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='orange',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='orange',command=iExit).grid(row=0,column=3)

###################################Calculator Display################################################################################




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################
txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='orange',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='orange',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='orange',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='orange',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='orange',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='orange',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='orange',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='orange',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='orange',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='orange',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='orange',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='orange',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='orange',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='orange',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='orange',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='orange',command=lambda:btnClick('/')).grid(row=5,column=3)



root.mainloop()
