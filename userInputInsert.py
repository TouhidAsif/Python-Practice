import  MySQLdb
from MySQLdb import *

try:
    con=MySQLdb.Connect(host="localhost",user="root",password="root",database="pythondb")
    print("connection success...")
    eid=int(input("enter employee id"))
    ename=input("enter your name")
    edept=input("enter department")
    esalary=int(input("your slary"))


    sql="insert into employee values ('%d','%s','%s','%d')"
    value=(eid,ename,edept,esalary)

    cur=con.cursor()
    cur.execute(sql % value)
    con.commit()
    print("record inserted",cur.rowcount)

except Exception as ex:
    print(ex)

finally:
    con.close()
    print("connection closed")