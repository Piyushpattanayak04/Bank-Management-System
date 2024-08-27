import os
import pickle
from tkinter import *
from tkinter import messagebox

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
                            print("Record Updated")
                            pickle.dump(data,f1)
                        else:
                            messagebox.showinfo("Bank System","Invalid Credentials")
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
    password_entry=Entry(dep_root,textvariable=pin_value).grid(row=2,column=5)
    n_2000_entry=Entry(dep_root,textvariable=n_2000_value).grid(row=3,column=5)
    n_500_entry=Entry(dep_root,textvariable=n_500_value).grid(row=4,column=5)
    n_200_entry=Entry(dep_root,textvariable=n_200_value).grid(row=5,column=5)
    n_100_entry=Entry(dep_root,textvariable=n_100_value).grid(row=6,column=5)

    Button(dep_root,text="Submit",command=dep_main).grid(row=8,column=5)

    dep_root.mainloop()