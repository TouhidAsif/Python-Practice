import  MySQLdb
from MySQLdb import *

try:
    con=MySQLdb.Connect(host="localhost",user="root",password="root",database="pythondb")
    print("connection success...")
    sql="insert into employee values (103,'asiftouhid','bba',23000)"
    cur=con.cursor()
    cur.execute(sql)
    con.commit()
    print("record inserted",cur.rowcount)

except Exception as ex:
    print(ex)