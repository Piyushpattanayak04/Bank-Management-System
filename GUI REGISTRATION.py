from tkinter import *
def register(): 

    reg_root=Tk()
    reg_root.geometry("564x344")
    Label(reg_root,text="USER REGISTRATION",font="comicsansms 30 bold",pady=15).grid(row=0,column=3)

    def reg_2():
    
        name=name_value.get()
        print(name)




    name=Label(reg_root,text="Name").grid(row=1,column=2)
    phone=Label(reg_root,text="Phone").grid(row=2,column=2)
    account_type=Label(reg_root,text="Account Type").grid(row=3,column=2)
    address=Label(reg_root,text="Address").grid(row=4,column=2)
    pin=Label(reg_root,text="Set 6 Digit Pin").grid(row=5,column=2)
    dob=Label(reg_root,text="Date Of Birth").grid(row=6,column=2)


    name_value=StringVar()
    phone_value=IntVar()
    account_type_value=StringVar()
    address_value=StringVar()
    pin_value=IntVar()
    dob_value=StringVar()


    nameentry=Entry(reg_root,textvariable=name_value).grid(row=1,column=3)
    phoneentry=Entry(reg_root,textvariable=phone_value).grid(row=2,column=3)
    genderentry=Entry(reg_root,textvariable=account_type_value).grid(row=3,column=3)
    emergencyentry=Entry(reg_root,textvariable=address_value).grid(row=4,column=3)
    pin_entry=Entry(reg_root,textvariable=pin_value).grid(row=5,column=3)
    dob_entry=Entry(reg_root,textvariable=dob_value).grid(row=6,column=3)

    reg_btn=Button(reg_root,text="Submit",command=reg_2).grid(row=7,column=3)




    reg_root.mainloop()



register()