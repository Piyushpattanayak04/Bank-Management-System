from tkinter import *
def balance():
    def bal_main():
        bal_root.destroy()

        f=open("bank.dat","rb")
        f.seek(0)

        customer_id=int(input("Enter Customer ID : "))
        pin=int(input("Enter 6 Digit Pin To Proceed: "))

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
                            messagebox.showinfo("Bank System","Invalid Credentails ")

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