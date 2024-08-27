from tkinter import*
def money_transfer():

    def mt_main():
        mt_root.destroy()

        customer_id=customer_id_value.get()
        pin=pin_value.get()
        upi_address=upi_id_value.get()
        total_amount=total_amount_value.get()

        f=open("bank.dat","rb")
        f1=open("money_transfer_temp.dat","wb")
        f.seek(0)
        try:
            while True :
                data=pickle.load(f)
                for i in data:
                    if i==customer_id:
                        if data[i][2]==pin:
                            net_amount=data[i][3]-total_amount
                            if net_amount<=0:
                                messagebox.showinfo("Bank System","Not Enough Balance To Transfer")
                            else:
                                data[i][3]=net_amount
                                pickle.dump(data,f1)
                                messagebox.showinfo("Bank System","Amount Transferred Sucessfully")
                        else:
                            messagebox.showinfo("Bank System","Invalid Credentials")
                    elif i!=customer_id:
                        pickle.dump(data,f1)

        except EOFError:
            f.close()
            f1.close()
            os.remove("bank.dat")
            os.rename("money_transfer_temp.dat","bank.dat")


    mt_root=Tk()
    mt_root.geometry("644x344")

    customer_id_value=IntVar()
    upi_id_value=StringVar()
    total_amount_value=IntVar()
    pin_value=IntVar()

    Label(mt_root,text="MONEY TRANSFER",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    customer_id=Label(mt_root,text="Customer ID").grid(row=1,column=2)
    upi_id=Label(mt_root,text="Reciever UPI ID").grid(row=2,column=2)
    total_amount=Label(mt_root,text="Amount To Be Transferred").grid(row=3,column=2)
    pin=Label(mt_root,text="PIN").grid(row=4,column=2)

    customer_identry_entry=Entry(mt_root,textvariable=customer_id_value).grid(row=1,column=3)
    upi_identry_entry=Entry(mt_root,textvariable=upi_id_value).grid(row=2,column=3)
    total_amountentry=Entry(mt_root,textvariable=total_amount_value).grid(row=3,column=3)
    pin_entry=Entry(mt_root,textvariable=pin_value,show="*").grid(row=4,column=3)

    Button(mt_root,text="Submit",command=mt_main).grid(row=6,column=3)

    mt_root.mainloop()