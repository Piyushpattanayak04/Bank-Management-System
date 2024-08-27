import os
import pickle
import random as r
from datetime import date
from tkinter import *
from tkinter import messagebox
import pyttsx3
from reportlab.pdfgen import canvas 

database={}

def register():

    def reg_main():
        reg_root.destroy()

        name=name_value.get()
        account_type=account_type_value.get()
        address=address_value.get()
        pin=pin_value.get()
        dob=dob_value.get()
        customer_id=r.randint(10000,99999)
        account_number=r.randint(10000000000,99999999999)
        cif_number=r.randint(1000000000,9999999999)
        balance=0
        opening_date=date.today().strftime("%d/%m/%Y")
        database[customer_id]=[account_number,name,pin,balance,account_type,address,opening_date,cif_number,dob]

        f=open("bank.dat","wb")
        pickle.dump(database,f)
        f.close()

        a=str(customer_id)
        messagebox.showinfo("Bank System","Account Created Sucessfully . Your Customer ID is"+a)
       

    reg_root=Toplevel(root)
    reg_root.geometry("564x344")
    reg_root.title("Registration Window")
    Label(reg_root,text="USER REGISTRATION",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    name_value=StringVar()
    account_type_value=StringVar()
    address_value=StringVar()
    dob_value=StringVar()
    pin_value=IntVar()
    phone_value=IntVar()
    

    name=Label(reg_root,text="Name").grid(row=1,column=2)
    phone=Label(reg_root,text="Phone").grid(row=2,column=2)
    account_type=Label(reg_root,text="Account Type").grid(row=3,column=2)
    address=Label(reg_root,text="Address").grid(row=4,column=2)
    pin=Label(reg_root,text="Set 6 Digit Pin").grid(row=5,column=2)
    dob=Label(reg_root,text="Date Of Birth").grid(row=6,column=2)

    name_entry=Entry(reg_root,textvariable=name_value).grid(row=1,column=3)
    phone_entry=Entry(reg_root,textvariable=phone_value).grid(row=2,column=3)
    account_type__entry=Entry(reg_root,textvariable=account_type_value).grid(row=3,column=3)
    address_entry=Entry(reg_root,textvariable=address_value).grid(row=4,column=3)
    pin_entry=Entry(reg_root,textvariable=pin_value,show="*").grid(row=5,column=3)
    dob_entry=Entry(reg_root,textvariable=dob_value).grid(row=6,column=3)

    Button(reg_root,text="Submit",command=reg_main).grid(row=7,column=3)

    reg_root.mainloop()

def deposit():

    def dep_main():
        dep_root.destroy()

        f=open("bank.dat","rb")
        f1=open("deposit_temp.dat","wb")
        f.seek(0)

        customer_id=customer_id_value.get()
        pin=pin_value.get()
        try:
            while True :
                data=pickle.load(f)
                for i in data:
                    if i==customer_id:
                        if data[i][2]==pin:
                            n2000=n_2000_value.get()
                            n500=n_500_value.get()    
                            n200=n_200_value.get()  
                            n100=n_100_value.get() 
                            total_amount=(n2000*2000)+(n500*500)+(n200*200)+(n100*100)
                            net_amount=data[i][3]+total_amount
                            data[i][3]=net_amount
                            pickle.dump(data,f1)
                        else:
                            messagebox.showerror("Bank System","Invalid Credentials")
                    elif i!=customer_id:
                        pickle.dump(data,f1)
        except EOFError:
            f.close()
            f1.close()
            os.remove("bank.dat")
            os.rename("deposit_temp.dat","bank.dat")
            messagebox.showinfo("Bank System","Ammount Credited Sucessfully")

    dep_root=Toplevel(root)
    dep_root.geometry("444x344")
    Label(dep_root,text="DEPOSITION",font="comicsansms 30 bold",padx=10,pady=25).grid(row=0,column=5)

    customer_id_value=IntVar()
    pin_value=IntVar()
    n_2000_value=IntVar()
    n_500_value=IntVar()
    n_200_value=IntVar()
    n_100_value=IntVar()

    customer_id=Label(dep_root,text="Customer ID").grid(row=1,column=4)
    pin=Label(dep_root,text="PIN").grid(row=2,column=4)
    n_2000=Label(dep_root,text="No. Of 2000 notes").grid(row=3,column=4)
    n_500=Label(dep_root,text="No. Of 500 notes").grid(row=4,column=4)
    n_200=Label(dep_root,text="No. Of 200 notes").grid(row=5,column=4)
    n_100=Label(dep_root,text="No. Of 100 notes").grid(row=6,column=4)

    customer_identry_entry=Entry(dep_root,textvariable=customer_id_value).grid(row=1,column=5)
    pin_entry=Entry(dep_root,textvariable=pin_value,show="*").grid(row=2,column=5)
    n_2000_entry=Entry(dep_root,textvariable=n_2000_value).grid(row=3,column=5)
    n_500_entry=Entry(dep_root,textvariable=n_500_value).grid(row=4,column=5)
    n_200_entry=Entry(dep_root,textvariable=n_200_value).grid(row=5,column=5)
    n_100_entry=Entry(dep_root,textvariable=n_100_value).grid(row=6,column=5)

    Button(dep_root,text="Submit",command=dep_main).grid(row=8,column=5)

    dep_root.mainloop()

def withdrawl():

    def with_main():
        with_root.destroy() 

        customer_id=customer_id_value.get()
        pin=pin_value.get()
        total_amount=amount_value.get()

        f=open("bank.dat","rb")
        f1=open("withdrawl_temp.dat","wb")
        f.seek(0)
        try:
            while True :
                data=pickle.load(f)
                for i in data:
                    if i==customer_id:
                        if data[i][2]==pin:
                            net_amount=data[i][3]-total_amount
                            if net_amount<=0:
                                messagebox.showerror("Bank System","Not Enough Balance To Withdraw")
                            else:
                                data[i][3]=net_amount
                                pickle.dump(data,f1)
                                messagebox.showinfo("Bank System","Amount Debited Sucessfully")
                        else:
                            messagebox.showerror("Bank System","Invalid Credentials")
                    elif i!=customer_id:
                        pickle.dump(data,f1)        
        except EOFError:
            f.close()
            f1.close()
            os.remove("bank.dat")
            os.rename("withdrawl_temp.dat","bank.dat")


    with_root=Toplevel(root)
    with_root.geometry("444x344")

    customer_id_value=IntVar()
    amount_value=IntVar()
    pin_value=IntVar()

    Label(with_root,text="WITHDRAWL",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    customer_id=Label(with_root,text="Customer ID").grid(row=1,column=2)
    amount=Label(with_root,text="Amount To Withdraw").grid(row=2,column=2)
    pin=Label(with_root,text="PIN").grid(row=3,column=2)

    customer_id_entry=Entry(with_root,textvariable=customer_id_value).grid(row=1,column=3)
    amount_entry=Entry(with_root,textvariable=amount_value).grid(row=2,column=3)
    pin_entry=Entry(with_root,text=pin_value,show="*").grid(row=3,column=3)

    Button(with_root,text="Submit",command=with_main).grid(row=6,column=3)

    with_root.mainloop()

def balance():
    def bal_main():
        bal_root.destroy()

        f=open("bank.dat","rb")
        f.seek(0)

        customer_id=customer_id_value.get()
        pin=pin_value.get()
        name=name_value.get()

        try:
            while True:
                data=pickle.load(f)
                for i in data:
                    if i==customer_id:
                        if data[i][2]==pin: 
                            balance=data[i][3]
                            a="The Available balance is : "+str(balance)
                            messagebox.showinfo("Bank System",a)
                        else:
                            messagebox.showerror("Bank System","Invalid Credentails ")

        except EOFError:
            f.close()

    bal_root=Toplevel(root)
    bal_root.geometry("544x344")

    name_value=StringVar()
    customer_id_value=IntVar()
    pin_value=IntVar()

    Label(bal_root,text="BALANCE ENQUIRY",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    name=Label(bal_root,text="Name").grid(row=1,column=2)
    customer_id=Label(bal_root,text="Customer ID").grid(row=2,column=2)
    pin=Label(bal_root,text="PIN").grid(row=3,column=2)

    nameentry=Entry(bal_root,textvariable=name_value).grid(row=1,column=3)
    customer_identry=Entry(bal_root,textvariable=customer_id_value).grid(row=2,column=3)
    pin_entry=Entry(bal_root,textvariable=pin_value,show="*").grid(row=3,column=3)


    Button(bal_root,text="Submit",command=bal_main).grid(row=6,column=3)


    bal_root.mainloop()

def passbook():
    def pb_main():
        pb_root.destroy()

        f=open("bank.dat","rb")
        id=customer_id_value.get()
        pin=pin_value.get()
        flag=0
        try:
            while True:
                s=pickle.load(f)
                for i in s:
                    if i==id:
                        if s[i][2]==pin:
                            name=s[i][1]
                            acc_type=s[i][4]
                            acc_number=s[i][0]
                            cif=s[i][7]
                            address=s[i][5]
                            dob=s[i][8]
                            doj=s[i][6]
                            balance=s[i][3]
                            flag=1
                        else:
                            messagebox.showerror("Bank System","Invalid Credentails ")


        except EOFError:
            f.close()
        if flag==1:
            c=canvas.Canvas("Passbook.pdf", pagesize=(500,250))
            c.setFont("Helvetica",18)
            c.setTitle("PASSBOOK")

            c.line(10,10,10,240)
            c.line(10,240,490,240)
            c.line(490,240,490,10)
            c.line(490,10,10,10)

            c.drawString(180,210,"D.A.V UNION BANK")
            c.setFont("Helvetica",12)
            c.drawString(20,160,"Account Type :"+acc_type)
            c.drawString(20,140,"CIF :"+str(cif))
            c.drawString(20,120,"Account Number :"+str(acc_number))
            c.drawString(20,100,"Customer Name : "+name)
            c.drawString(20,80,"Address :"+address)
            c.drawString(20,60,"DOB :"+dob)
            c.drawString(20,40,"Balance :"+str(balance))
            c.drawString(340,160,"Pokhariput")
            c.drawString(340,140,"AT/PO - Pokhariput")
            c.drawString(340,100,"Phone : 0674-45875")
            c.drawString(340,80,"Email : PUB@hotmail.com")
            c.drawString(340,60,"Branch Code : 547784")
            c.drawString(340,40,"Date Of Issue :"+doj)

            c.save()
            print(" ")
            messagebox.showinfo("Bank System","Passbook Has Been generated Sucessfully")
        
        else:
            messagebox.showerror("Bank System","Invalid Customer ID")

        

 

    pb_root=Toplevel(root)
    pb_root.geometry("644x244")

    customer_id_value=IntVar()
    pin_value=IntVar()

    Label(pb_root,text="PASSBOOK GENERATION",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    customer_id=Label(pb_root,text="Customer ID ").grid(row=1,column=2)
    pin=Label(pb_root,text="PIN").grid(row=2,column=2)

    
    customer_identry=Entry(pb_root,textvariable=customer_id_value).grid(row=1,column=3)
    pin_entry=Entry(pb_root,textvariable=pin_value,show="*").grid(row=2,column=3)


    Button(pb_root,text="Submit",command=pb_main).grid(row=6,column=3)


    pb_root.mainloop()

def closure():
    
    def clo_main():
        clo_root.destroy()
        if checkbox_value.get()==0:
            messagebox.showerror("Bank System","Please Click Checkbox To Confirm")
        else:
            f=open("bank.dat","rb")
            f1=open("closure_temp.dat","wb")
            name=name_value.get()
            customer_id=customer_id_value.get()
            pin=pin_value.get()
            

            try:
                while True:
                    data=pickle.load(f)
                    for i in data:
                        if customer_id!=i: 
                            pickle.dump(data,f1)
                              
                        a="Customer ID:"+str(customer_id)+" has been deleted sucessfully"
                        messagebox.showinfo("Bank System",a)

            except EOFError:
                f.close()
                f1.close()
                os.remove("bank.dat")
                os.rename("closure_temp.dat","bank.dat")



    clo_root=Toplevel(root)
    clo_root.geometry("584x344")

    name_value=StringVar()
    customer_id_value=IntVar()
    pin_value=IntVar()
    checkbox_value=IntVar()

    Label(clo_root,text="ACCOUNT CLOSURE",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    name=Label(clo_root,text="Name").grid(row=1,column=2)
    customer_id=Label(clo_root,text="Customer ID").grid(row=2,column=2)
    pin=Label(clo_root,text="PIN").grid(row=3,column=2)
  
    name_entry=Entry(clo_root,textvariable=name_value).grid(row=1,column=3)
    customer_id_entry=Entry(clo_root,textvariable=customer_id_value).grid(row=2,column=3)
    pin_entry=Entry(clo_root,textvariable=pin_value,show="*").grid(row=3,column=3)

    Checkbutton(clo_root,text="Do You Want To Delete The Account",variable=checkbox_value).grid(row=6,column=3)
    Button(clo_root,text="Submit",command=clo_main).grid(row=7,column=3)

    clo_root.mainloop()
    
def voice():
    engine = pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("rate", 125)
    engine.setProperty("voice", voices[1].id)
    engine.say("Welcome To The D A V Union Bank ")
    engine.say("Please Select Any Option To Continue ")
    engine.runAndWait()

def quit():
    root.destroy()
    print(" ")
    print("*"*162)
    print(" ")
    print(" "*75+"THANK YOU FOR VISITING OUR BANK : ] ")
    print(" ")
    print("*"*162)



root = Tk()
root.title("Bank Management system")
root.minsize(width=1000,height=400)
root.geometry("1920x1080")

c=Canvas(root,bg="gray",height=200,width=200)
filename=PhotoImage(file="BG1.png")
background_label=Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
c.pack()


headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="  Welcome to \n D.A.V Union Bank", bg='black', fg='white', font=('Courier',30))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = Button(root,text="REGISTER",bg='black', fg='white',font=20,command=register)
btn1.place(relx=0,rely=0.3, relwidth=0.25,relheight=0.1)
    
btn2 = Button(root,text="DEPOSIT",bg='black', fg='white',font=20,command=deposit)
btn2.place(relx=0,rely=0.46, relwidth=0.25,relheight=0.1)
    
btn3 = Button(root,text="WITHDRAWL",bg='black', fg='white',font=20,command=withdrawl)
btn3.place(relx=0,rely=0.62, relwidth=0.25,relheight=0.1)
    
btn5 = Button(root,text="BALANCE",bg='black', fg='white',font=20,command=balance)
btn5.place(relx=0.75,rely=0.3, relwidth=0.25,relheight=0.1)

btn6= Button(root,text="PASSBOOK",bg='black', fg='white',font=20,command=passbook)
btn6.place(relx=0.75,rely=0.46, relwidth=0.25,relheight=0.1)

btn8= Button(root,text="CLOSURE",bg='black', fg='white',font=20,command=closure)
btn8.place(relx=0.75,rely=0.62, relwidth=0.25,relheight=0.1)

btn9= Button(root,text="QUIT",bg='white', fg='red',command=quit)
btn9.place(relx=0.55,rely=0.78, relwidth=0.07,relheight=0.1)

btn10=Button(root,text="VOICE",bg='white', fg='red',command=voice)
btn10.place(relx=0.37,rely=0.78, relwidth=0.07,relheight=0.1)

root.mainloop()
