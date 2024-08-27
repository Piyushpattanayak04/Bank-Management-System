from tkinter import *
from tkinter import messagebox
import pickle
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

            c.drawString(140,210,"D.A.V UNION BANK")
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


btn1 = Button(root,text="REGISTER",bg='black', fg='white',font=20,command=passbook)
btn1.place(relx=0,rely=0.3, relwidth=0.25,relheight=0.1)
    


root.mainloop()