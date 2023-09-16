from tkinter import *
import MySQLdb

class MyDataBase:
    def __init__(self):
        self.con = MySQLdb.Connect(host="localhost", user="root", password="root", database="pythondb")
        print("Connection success...")
        self.autoId()  # Automatically generate a new employee ID

    def autoId(self):
        sql = "select max(id) from employee"
        self.cur = self.con.cursor()
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.maxid = result[0] if result[0] else 100  # Default to 100 if no records exist
        self.maxid += 1

    def saveData(self):
        sql = "insert into employee values ('%d','%s','%s','%d')"
        self.cur = self.con.cursor()
        value = (self.maxid, txtename.get(), txtdept.get(), int(txtsalary.get()))
        self.cur.execute(sql % value)
        self.con.commit()
        print("Record inserted", self.cur.rowcount)
        self.con.close()
        print('Connection closed....')

myroot = Tk()
myroot.geometry('600x600')
myroot.maxsize(600, 600)
myroot.minsize(600, 600)
myroot.title("Employee Registration Form")

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

M1 = MyDataBase()  # Create an instance of the MyDataBase class

btnsave = Button(text='Save', font=('Arial,10,bold'), fg="black", command=M1.saveData)
btnsave.grid(row=6, column=1)

myroot.mainloop()