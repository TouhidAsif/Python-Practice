import myconnection as ms
import model
import employeedao as empdao

con1 = ms.MyConnection.getConnection()
print("connection success!")
E1 = model.Employee()
eid=int(input("Enter employee id: "))
ename=input("Enter your name: ")
edept=input("Enter department: ")
esalary=int(input("Enter your salary: "))



E1.setid(eid)
E1.setname(ename)
E1.setdept(edept)
E1.setsalary(esalary)
ed = empdao.EmployeeDao()
ed.insertEmployee(E1)
print("record inserted............")
