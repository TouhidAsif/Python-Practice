from tkinter import *
import MySQLdb
def saveData():
    con = MySQLdb.Connect(host="localhost", user="root", password="root", database="pythondb")
    print("connection success...")
    sql = "insert into employee values ('%d','%s','%s','%d')"
    cur=con.cursor()
    value=(int(txtid.get()),txtename.get(),txtdept.get(),int(txtsalary.get()))
    cur.execute(sql % value)
    con.commit()
    print("record inserted", cur.rowcount)
    con.close()
    print('connection close....')


myroot = Tk()
myroot.geometry('600x600')
myroot.maxsize(600, 600)
myroot.minsize(600, 600)
myroot.title("Employee Registration Form")

lb1 = Label(text="Enter Employee Id", font=('Arial,10,bold'), fg="red")
lb1.grid(row=0, column=0)
eid = IntVar()
txtid = Entry(textvariable=eid, font=('Arial,10,bold'), fg="blue")
txtid.grid(row=0, column=1)

lb2 = Label(text="Enter Employee Name", font=('Arial,10,bold'), fg="red")
lb2.grid(row=1, column=0)
ename = StringVar()
txtename = Entry(textvariable=ename, font=('Arial,10,bold'), fg="blue")
txtename.grid(row=1, column=1)

lb3 = Label(text="Enter Employee Department", font=('Arial,10,bold'), fg="red")
lb3.grid(row=2, column=0)
edept = StringVar()
txtdept = Entry(textvariable=edept, font=('Arial,10,bold'), fg="blue")
txtdept.grid(row=2, column=1)

lb4 = Label(text="Enter Employee Salary", font=('Arial,10,bold'), fg="red")
lb4.grid(row=3, column=0)
esalary = StringVar()
txtsalary = Entry(textvariable=esalary, font=('Arial,10,bold'), fg="blue")
txtsalary.grid(row=3, column=1)

btnsave=Button(text='Save',font=('Arial,10,bold'), fg="black",command=saveData)
btnsave.grid(row=6,column=1)

myroot.mainloop()
