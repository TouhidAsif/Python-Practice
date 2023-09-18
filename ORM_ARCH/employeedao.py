import myconnection as mcon
import model


class EmployeeDao:

    def __init__(self):
        self.con = mcon.MyConnection.getConnection()
        self.cur = self.con.cursor()

    def insertEmployee(self, E):
        try:
            sql = "insert into employee values('%d','%s','%s','%d')"
            value = (E.getid(), E.getname(), E.getdept(), E.getsalary())
            self.cur.execute(sql % value)
            self.con.commit()
        except Exception as obj:
            print(obj)

    def searchEmployee(self, empid):
        try:
            sql = "select * from employee where id=%d"
            self.cur.execute(sql % empid)
            result = self.cur.fetchone()
            E1 = model.Employee()
            E1.setid(result[0])
            E1.setname(result[1])
            E1.setdept(result[2])
            E1.setsalary(result[3])
            return E1
        except Exception as msg:
            print(msg)
