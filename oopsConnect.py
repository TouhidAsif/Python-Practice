import  MySQLdb
from MySQLdb import *
class MyDataBase:
    def __init__(self):
        self.con=MySQLdb.Connect(host="localhost",user="root",password="root",database="pythondb")
        print("connection success...")
    def insertData(self,eid,ename,edept,esalary):
        sql="insert into employee values ('%d','%s','%s','%d')"
        value=(eid,ename,edept,esalary)
        self.cur=self.con.cursor()
        self.cur.execute(sql % value)
        print("record inserted: ",self.cur.rowcount)
        self.con.commit()
    def conClose(self):
        self.con.close()

M1=MyDataBase()

eid=int(input("Enter employee id: "))
ename=input("Enter your name: ")
edept=input("Enter department: ")
esalary=int(input("Enter your salary: "))

M1.insertData(eid,ename,edept,esalary)

M1.conClose()