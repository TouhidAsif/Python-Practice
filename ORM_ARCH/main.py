import myconnection as ms
import model
import employeedao as empdao

con1 = ms.MyConnection.getConnection()
print("connection success!")
E1=model.Employee()


#.......................search All......................

ed=empdao.EmployeeDao()
myList1=ed.searchAll()
for emp in myList1:
    print(emp.getid(),end=" ")
    print(emp.getname(), end=" ")
    print(emp.getdept(), end=" ")
    print(emp.getsalary())





#.................update code.................

# eid=int(input("Enter employee id: "))
# ename=input("Enter your name for update: ")
# edept=input("Enter department for update: ")
# esalary=int(input("Enter your salary for update: "))
#
# E1.setid(eid)
# E1.setname(ename)
# E1.setdept(edept)
# E1.setsalary(esalary)
# ed=empdao.EmployeeDao()
# ed.updateEmployee(E1)
# print("record updated")


# ...................for delete one by id...................

# eid=int(input("Enter employee id for delete: "))
# ed=empdao.EmployeeDao()
# E=ed.searchEmployee(eid)
#
# if E is not None:
#     print("emp id :", E.getid())
#     print("emp name :", E.getname())
#     print("emp dept :", E.getdept())
#     print("emp salary :", E.getsalary())
#     choice=input("Are you sure want to delete (yes/no)")
#     if(choice=='yes'):
#         ed.deleteEmployee(eid)
#         print("record deleted")
#
# else:
#     print(f"No employee found with ID {eid}")



# .................for search one by id........................

# eid=int(input("Enter employee id for search: "))
# ed=empdao.EmployeeDao()
# E=ed.searchEmployee(eid)
#
# if E is not None:
#     print("emp id :", E.getid())
#     print("emp name :", E.getname())
#     print("emp dept :", E.getdept())
#     print("emp salary :", E.getsalary())
# else:
#     print(f"No employee found with ID {eid}")





# ......................for insert...........................

# eid=int(input("Enter employee id: "))
# ename=input("Enter your name: ")
# edept=input("Enter department: ")
# esalary=int(input("Enter your salary: "))
#
#
#
# E1.setid(eid)
# E1.setname(ename)
# E1.setdept(edept)
# E1.setsalary(esalary)
# ed = empdao.EmployeeDao()
# ed.insertEmployee(E1)
# print("record inserted............")
