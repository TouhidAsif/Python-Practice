import myconnection as ms
import model
import employeedao as empdao

con1 = ms.MyConnection.getConnection()
print("connection success!")
E1 = model.Employee()
E1.setid(201)
E1.setname("Asif")
E1.setdept("ICT")
E1.setsalary(100000)
ed = empdao.EmployeeDao()
ed.insertEmployee(E1)
print("record inserted............")
