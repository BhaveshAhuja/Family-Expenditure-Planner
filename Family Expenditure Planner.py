from tkinter import *
import sqlite3
from tkinter import messagebox
import tkinter as tk
import os

root=tk.Tk()
x=tk.IntVar()

conn=sqlite3.connect('fam1.db')
'''conn.execute("CREATE TABLE FAMILY (NAME TEXT NOT NULL,SURNAME TEXT NOT NULL,MEMBERS INT NOT NULL,ANNUAL INT NOT NULL,LASTMONTH INT NOT NULL,PROPER INT NOT NULL,\
                GOLD INT NOT NULL,FOOD INT NOT NULL,ELECTRICITY INT NOT NULL,EDUCATION INT NOT NULL,COSMETICS INT NOT NULL,LUXURY INT NOT NULL,TRAVEL INT NOT NULL, \
                OTHER INT NOT NULL,NUMBER INT NOT NULL,EMAIL TEXT NOT NULL,MESSAGE TEXT);")'''
name,surname,members,annual,lastMonth,proper,gold,food,electricity,education,cosmetics,luxury,travel,other,uid,upass,email,number,plmessage=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0



def databasefun(total):
    
    global name,surname,members,annual,lastMonth,proper,gold,food,electricity,education,cosmetics,luxury,travel,other,number,email
    total.quit()
    total.destroy()
    conn.execute("INSERT INTO FAMILY (NAME,SURNAME,MEMBERS,ANNUAL,LASTMONTH,PROPER,GOLD,FOOD,ELECTRICITY,EDUCATION,COSMETICS,LUXURY,TRAVEL,OTHER,NUMBER,EMAIL) \
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(name,surname,members,annual,lastMonth,proper,gold,food,electricity,education,cosmetics,luxury,travel,other,number,email));
    conn.commit()
    

    #Fees:
    fee=tk.Tk()
    fee.title("FAMILY EXPENDITURE PLANNING-CUSTOMER-PLANNER FEES")
    width,height=fee.winfo_screenwidth(),fee.winfo_screenheight()
    fee.geometry('%dx%d+0+0'%(width,height))
    fee["bg"]="#b3e6ff"
    Label(fee,text='''
Thank you for working with us!

You can pay us through following services:
Transfer your money to Bank Account Number: 783920001941
Pay by using Patym on Mobile Number: 9702379158
Pay on Tez by Google using UPI ID: bgahuja19@okhdfcbank

As soon as we will receive our fees, our experts will start working to maximize
your savings and minimize expenditure

You can view the expret suggestion in Customer-Message
Use ID as your email''',font="Roman 15 bold italic",height=15,width=100,bg="yellow").place(x=240,y=100)
    
    fee.mainloop()

    
##root=tk.Tk()
##x=tk.IntVar()    
def PlannerClick():
    global uid,plmessage
    global upass
    
    root.quit()
    #root.destroy()
    plan=tk.Tk()
    plan.title("FAMILY EXPENDITURE PLANNING-PLANNER")
    width,height=plan.winfo_screenwidth(),plan.winfo_screenheight()
    plan.geometry('%dx%d+0+0'%(width,height))
    plan["bg"]="#b3e6ff"
    lab1=tk.Label(plan,text="",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=2,column=0)
    lab2=tk.Label(plan,text="",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=3,column=0)
    label1=tk.Label(plan,text="User Name",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=4,column=1)
    label1=tk.Label(plan,text="Password",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=5,column=1)
    t1=Entry(plan)
    t1.grid(row=4,column=2,pady=5)
    t2=Entry(plan,show="●")
    t2.grid(row=5,column=2,pady=5)

    Button(plan,text="<< OPEN DATABASE >>",width=20,height=3,command=plan.quit,bg='#d5d9e0',font='times 10 bold').place(x=600,y=500)
    plan.mainloop()

    uid=t1.get()
    upass=t2.get()
    #print(uid,upass)
    plan.destroy()
    
    if(uid == "Anubhav" and upass == "mayakaal"):
        plmsg=tk.Tk()
        plmsg.title("FAMILY EXPENDITURE PLANNING-PLANNER")
        width,height=plmsg.winfo_screenwidth(),plmsg.winfo_screenheight()
        plmsg.geometry('%dx%d+0+0'%(width,height))
        plmsg["bg"]="#b3e6ff"

        lab1=tk.Label(plmsg,text="Email ID",height=2,width=30,bg="#b3e6ff",font="times 15 bold").place(x=0,y=85)
        lab1=tk.Label(plmsg,text="Message after analysis",height=2,width=30,bg="#b3e6ff",font="times 15 bold").place(x=8,y=150)
        t1=Entry(plmsg,width=100)
        t1.place(x=300,y=100)
        t2=Text(plmsg,width=150,height=10)
        t2.place(x=80,y=200)
        os.system("DBBrowser\DBBrowser.exe")
        os.system("taskkill /f /im C:\WINDOWS\system32\cmd.exe")
        Button(plmsg,text="<< SUBMIT MESSAGE >>",width=20,height=3,command=plmsg.quit,bg='#d5d9e0',font='times 10 bold').place(x=600,y=500)
        plmsg.mainloop()
        plemail=t1.get()
        plmessage=t2.get("1.0","end-1c")
        conn.execute("UPDATE FAMILY SET MESSAGE=(?) WHERE EMAIL=(?)",(plmessage,plemail));
        conn.commit()
        print(plmessage,plemail)
        
    else:
        if(uid!="Anubhav"):
            messagebox.showinfo("Wrong Details", "Wrong User ID")
        elif(upass!="mayakaal"):
            messagebox.showinfo("Wrong Details", "Wrong User Password")
    
    
    
def messageClick():
    root.quit()
    #root.destroy()
    emessage=tk.Tk()
    emessage.title("FAMILY EXPENDITURE PLANNING-CUSTOMER-MESSAGE")
    width,height=emessage.winfo_screenwidth(),emessage.winfo_screenheight()
    emessage.geometry('%dx%d+0+0'%(width,height))
    emessage["bg"]="#b3e6ff"
    label=tk.Label(emessage,text="Email ID",height=2,width=30,bg="#b3e6ff",font="times 15 bold").place(x=0,y=85)
    t=Entry(emessage,width=100)
    t.place(x=300,y=100)
    Button(emessage,text="<< GET MESSAGE >>",width=20,height=3,command=emessage.quit,bg='#d5d9e0',font='times 10 bold').place(x=500,y=500)
    emessage.mainloop()
    cemail=t.get()
    emessage.destroy()

    message=tk.Tk()
    message.title("FAMILY EXPENDITURE PLANNING-CUSTOMER-MESSAGE")
    width,height=message.winfo_screenwidth(),message.winfo_screenheight()
    message.geometry('%dx%d+0+0'%(width,height))
    message["bg"]="#b3e6ff"
    x=conn.execute("SELECT MESSAGE FROM FAMILY WHERE EMAIL = '%s'" % cemail);
    Label(message,text=x.fetchone(),font="Roman 15 bold italic",height=12,width=100,bg="yellow").place(x=240,y=100)
    Label(message,text='''NOTE:
If above space is blank, then Email ID is either incorrect or you have not asked for help yet.
if None appears above, then you have not yet paid the fees.''',font="Roman 15 bold italic",height=6,width=100,bg="yellow").place(x=240,y=500)
        
def helpClick():
    global name,surname,members,annual,lastMonth,proper,gold,food,electricity,education,cosmetics,luxury,travel,other,email,number,x
    #Personal Information:
    root.quit()
    #root.destroy()
    info=tk.Tk()
    info.title("FAMILY EXPENDITURE PLANNING-CUSTOMER-INFORMATION")
    width,height=info.winfo_screenwidth(),info.winfo_screenheight()
    info.geometry('%dx%d+0+0'%(width,height))
    info["bg"]="#b3e6ff"
    lab=tk.Label(info,text="PERSONAL DETAILS",height=5,width=30,bg="#b3e6ff",font="times 15 bold italic underline").grid(row=0,column=0,columnspan=3)
    label1=tk.Label(info,text="First Name",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=2,column=0)
    label2=tk.Label(info,text="Last Name",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=3,column=0)
    label3=tk.Label(info,text="Number Of Family Members",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=4,column=0)
    label4=tk.Label(info,text="Contact Number",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=5,column=0)
    label5=tk.Label(info,text="Email ID",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=6,column=0)

    t1=Entry(info)
    t1.grid(row=2,column=1,pady=5)
    t2=Entry(info)
    t2.grid(row=3,column=1,pady=5)
    t3=Entry(info)
    t3.grid(row=4,column=1,pady=5)
    t4=Entry(info)
    t4.grid(row=5,column=1,pady=5)
    t5=Entry(info)
    t5.grid(row=6,column=1,pady=5)

    Button(info,text="<< NEXT >>",width=10,height=3,command=info.quit,bg='#d5d9e0',font='times 10 bold').place(x=500,y=500)

    info.mainloop()

    
    name=t1.get()
    surname=t2.get()
    members=t3.get()
    number=t4.get()
    email=t5.get()
    if(name.isalpha() and surname.isalpha() and members.isdigit() and number.isdigit() and len(number)==10 and '@' in email and '.' in email):
        pass
    else:
        messagebox.showinfo("Wrong Details", "Please enter correct information and close this window")
    info.destroy()

    #Income Details:
    income=tk.Tk()
    income.title("FAMILY EXPENDITURE PLANNING-CUSTOMER-INFORMATION")
    width,height=income.winfo_screenwidth(),income.winfo_screenheight()
    income.geometry('%dx%d+0+0'%(width,height))
    income["bg"]="#b3e6ff"
    lab=tk.Label(income,text="FAMILY INCOME DETAILS",height=5,width=30,bg="#b3e6ff",font="times 15 bold italic underline").grid(row=0,column=0,columnspan=4)
    rlabel=tk.Label(income,text="Work",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=2,column=0)
    Radiobutton(income,text="Business",variable=x,value="1").place(x=370,y=135)
    Radiobutton(income,text="Service",variable=x,value="2").place(x=570,y=135)
    label1=tk.Label(income,text="Average Annual Income",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=3,column=0)
    label2=tk.Label(income,text="Last Month Income",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=4,column=0)
    label3=tk.Label(income,text="Property in Rupees",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=5,column=0)
    label3=tk.Label(income,text="Gold in Rupees",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=6,column=0)

    t1=Entry(income)
    t1.grid(row=3,column=1,pady=5)
    t2=Entry(income)
    t2.grid(row=4,column=1,pady=5)
    t3=Entry(income)
    t3.grid(row=5,column=1,pady=5)
    t4=Entry(income)
    t4.grid(row=6,column=1,pady=5)

    Button(income,text="<< NEXT >>",width=10,height=3,command=income.quit,bg='#d5d9e0',font='times 10 bold').place(x=500,y=500)

    income.mainloop()
    annual=t1.get()
    lastMonth=t2.get()
    proper=t3.get() #property
    gold=t4.get()
    if(annual.isdigit() and lastMonth.isdigit() and proper.isdigit() and gold.isdigit()):
        pass
    else:
        messagebox.showinfo("Wrong Details", "Please enter correct information and close this window")

    income.destroy()

    #Expenditure Details:
    expense=tk.Tk()
    expense.title("FAMILY EXPENDITURE PLANNING-CUSTOMER-INFORMATION")
    width,height=expense.winfo_screenwidth(),expense.winfo_screenheight()
    expense.geometry('%dx%d+0+0'%(width,height))
    expense["bg"]="#b3e6ff"

    lab=tk.Label(expense,text="EXPENDITURE DETAILS",height=5,width=30,bg="#b3e6ff",font="times 15 bold italic underline").grid(row=0,column=0,columnspan=3)
    label1=tk.Label(expense,text="Food Expenses",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=2,column=0)
    label2=tk.Label(expense,text="Electricity Bills",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=3,column=0)
    label3=tk.Label(expense,text="Education Fees",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=4,column=0)
    label4=tk.Label(expense,text="Cosmetics",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=5,column=0)
    label5=tk.Label(expense,text="Luxury Expenses",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=6,column=0)
    label6=tk.Label(expense,text="Travelling Expenses",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=7,column=0)
    label7=tk.Label(expense,text="Other",height=2,width=30,bg="#b3e6ff",font="times 15 bold").grid(row=8,column=0)

    t1=Entry(expense)
    t1.grid(row=2,column=1,pady=5)
    t2=Entry(expense)
    t2.grid(row=3,column=1,pady=5)
    t3=Entry(expense)
    t3.grid(row=4,column=1,pady=5)
    t4=Entry(expense)
    t4.grid(row=5,column=1,pady=5)
    t5=Entry(expense)
    t5.grid(row=6,column=1,pady=5)
    t6=Entry(expense)
    t6.grid(row=7,column=1,pady=5)
    t7=Entry(expense)
    t7.grid(row=8,column=1,pady=5)

    Button(expense,text="<< NEXT >>",width=10,height=3,command=expense.quit,bg='#d5d9e0',font='times 10 bold').place(x=500,y=500)

    expense.mainloop()
    food=t1.get()
    electricity=t2.get()
    education=t3.get()
    cosmetics=t4.get()
    luxury=t5.get()
    travel=t6.get()
    other=t7.get()
    #if(expense.isdigit() and food.isdigit() and electricity.isdigit() and education.isdigit() and cosmetics.isdigit() and luxury.isdigit() and travel.isdigit() and other.isdigit()):
        #pass
    #else:
        #messagebox.showinfo("Wrong Details", "Please enter correct information and close this window")

    expense.destroy()

    #Total Cost:
    total=tk.Tk()
    total.title("FAMILY EXPENDITURE PLANNING-CUSTOMER-DECISION")
    width,height=total.winfo_screenwidth(),total.winfo_screenheight()
    total.geometry('%dx%d+0+0'%(width,height))
    total["bg"]="#b3e6ff"
    if(int(annual)<100000):
        Label(total,text='''We will configure your entire details and send you the correct expenditure planning made by our experts!
The total cost will be Rs.6590
If you want to get advice then click YES, or close the window''',font="Roman 15 bold italic",height=12,width=100,bg="yellow").place(x=240,y=100)

    else:
        Label(total,text='''We will configure your entire details and send you the correct expenditure planning made by our experts!
The total cost will be Rs.9260
If you want to get advice then click YES, or close the window''',font="Roman 15 bold italic",height=12,width=100,bg="yellow").place(x=240,y=100)
    
    Button(total,text="<< YES >>",width=10,height=3,command=lambda:databasefun(total),bg='#d5d9e0',font='times 10 bold').place(x=640,y=500)

    total.mainloop()
    #total.destroy()

def CustomerClick(file3,file4):
    #Customer Options
    
    cust=Toplevel()
    cust.title("FAMILY EXPENDITURE PLANNING-CUSTOMER")
    width,height=cust.winfo_screenwidth(),cust.winfo_screenheight()
    cust.geometry('%dx%d+0+0'%(width,height))

    cust["bg"]="#b3e6ff"

    Button(cust,image=file3,width=450,height=400,command=messageClick,relief="raise").place(x=200,y=200)
    Button(cust,image=file4,width=500,height=400,command=helpClick,relief="raise",bg="#347268").place(x=700,y=200)
    #Button(cust,image=file3,width=350,height=338,relief="raise").place(x=300,y=200)
    #Button(cust,image=file4,width=400,height=338,relief="raise").place(x=700,y=200)
    label1=Label(cust,text="PLANNED MESSAGE",width=41,height=3,font="times 15 bold italic underline",bg='#b3e6ff').place(x=200,y=120)
    label2=Label(cust,text="ENTER DETAILS",width=45,height=3,font="times 15 bold italic underline",bg='#b3e6ff').place(x=700,y=120)
    cust.mainloop()
    
root.title("FAMILY EXPENDITURE PLANNING")
width,height=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(width,height))
root["bg"]="yellow"
file1=PhotoImage(file='Customer.png')
file2=PhotoImage(file='Planner.png')
file3=PhotoImage(file='message.png')
file4=PhotoImage(file='help.png')
Button(root,image=file2,width=350,height=338,command=PlannerClick,relief="raise").place(x=300,y=200)
Button(root,image=file1,width=400,height=338,command=lambda : CustomerClick(file3,file4),relief="raise").place(x=700,y=200)
label1=Label(root,text="PLANNER",width=32,height=3,font="times 15 bold italic underline",bg='yellow').place(x=300,y=120)
label2=Label(root,text="CUSTOMER",width=36,height=3,font="times 15 bold italic underline",bg='yellow').place(x=700,y=120)
root.mainloop()
print(name,surname,members,annual,lastMonth,proper,gold,food,electricity,education,cosmetics,luxury,travel,other,uid,upass,x,plmessage)


'''
FINAL PROBLEMS TO BE DONE AFTER UT:
1. Expense wali window band nhi hui.  done
2. Message daalna h extra database mei.  KRNA H KHUDI
3. Message print bhi krna h customer ke message mei... uski id daalne k baad.
4. Email id wala block size badhana hai.  done
5. Open Database pe DBBrowser open toh hoga... but file khud ko open krni padegi. Toh uske liye try krte h.
6. Open Database mei dono saath mei open nhi hore, pehle database n fir message enter krne wali window, hua toh change karenge...
'''
