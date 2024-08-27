import pickle

from reportlab.pdfgen import canvas 

def passbook():
    f=open("bank.dat","rb")
    id=int(input("Enter Customer ID : "))
    try:
        while True:
            s=pickle.load(f)
            for i in s:
                if i==id:
                    name=s[i][1]
                    acc_type=s[i][4]
                    acc_number=s[i][0]
                    cif=s[i][7]
                    address=s[i][5]
                    dob=s[i][8]
                    doj=s[i][6]
                    balance=s[i][3]

    except EOFError:
        f.close()



    c=canvas.Canvas("Passbook.pdf", pagesize=(500,250))
    c.setFont("Helvetica",18)
    c.setTitle("PASSBOOK")

    c.line(10,10,10,240)
    c.line(10,240,490,240)
    c.line(490,240,490,10)
    c.line(490,10,10,10)

    c.drawString(140,210,"POKHARIPUT UNION BANK")
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
    print("Your Passbook Has Been Generated ")

passbook()