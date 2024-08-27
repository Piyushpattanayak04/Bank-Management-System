
from tkinter import *
def withdrawl():

    def with_main():
        
        with_root.destroy() 

        customer_id=customer_id_value.get()
        pin=pin_value.get()
        total_amount=amount_value.get()

        f=open("bank.dat","rb")
        f1=open("withdrwal_temp.dat","wb")
        f.seek(0)
        try:
            while True :
                data=pickle.load(f)
                for i in data:
                    if i==customer_id:
                        if data[i][2]==pin:
                            net_amount=data[i][3]-total_amount
                            if net_amount<=0:
                                messagebox.showinfo("Bank System","Not Enough Balance To Withdraw")
                            else:
                                data[i][3]=net_amount
                                pickle.dump(data,f1)
                                messagebox.showinfo("Bank System","Amount Debited Sucessfully")
                        else:
                            messagebox.showinfo("Bank System","Invalid Credentials")
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



