from tkinter import *
from tkinter import messagebox

def closure():
    
    def clo_main():
        clo_root.destroy()
        if checkbox_value.get()==0:
            messagebox.showerror("Bank System","Please Click Checkbox To Confirm")
        else:
            f=open("bank.dat","rb")
            f1=open("closure_temp.dat","wb")
            customer_id=int(input("Enter Customer ID : "))
            pin=int(input("Enter 6 Digit Pin To Proceed: "))
            try:
                while True:
                    data=pickle.load(f)
                    for i in data:
                        if data[i][2]==pin: 
                            if i!=customer_id:
                                pickle.dump(data,f1)
                                a="Customer ID:"+str(i)+" has been deleted sucessfully"
                                messagebox.showinfo("Bank System",a)  
                        else:
                            messagebox.showerror("Bank System","Invalid Credentails ")

            except EOFError:
                f.close()
                os.remove("bank.dat")
                os.rename("closure_temp.dat","bank.dat")



    clo_root=Toplevel(root)
    clo_root.geometry("584x344")

    name_value=StringVar()
    customer_id_value=IntVar()
    account_number_value=IntVar()
    pin_value=IntVar()
    checkbox_value=IntVar()

    Label(clo_root,text="ACCOUNT CLOSURE",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    name=Label(clo_root,text="Name").grid(row=1,column=2)
    customer_id=Label(clo_root,text="Customer ID").grid(row=2,column=2)
    account_number=Label(clo_root,text="Account Number ").grid(row=3,column=2)
    pin=Label(clo_root,text="PIN").grid(row=4,column=2)
  
    name_entry=Entry(clo_root,textvariable=name_value).grid(row=1,column=3)
    customer_id_entry=Entry(clo_root,textvariable=customer_id_value).grid(row=2,column=3)
    account_number_entry=Entry(clo_root,textvariable=account_number_value).grid(row=3,column=3)
    pin_entry=Entry(clo_root,textvariable=pin_value,show="*").grid(row=4,column=3)

    Checkbutton(clo_root,text="Do You Want To Delete The Account",variable=checkbox_value).grid(row=6,column=3)
    Button(clo_root,text="Submit",command=clo_main).grid(row=7,column=3)

    clo_root.mainloop()


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


btn1 = Button(root,text="REGISTER",bg='black', fg='white',font=20,command=closure)
btn1.place(relx=0,rely=0.3, relwidth=0.25,relheight=0.1)
    


root.mainloop()