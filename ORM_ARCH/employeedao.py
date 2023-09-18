import myconnection as mcon
import  model
class EmployeeDao:

    def __init__(self):
        self.con=mcon.MyConnection.getConnection()
        self.cur=self.con.cursor()
    def insertEmployee(self,E):
        try:
            sql="insert into employee values('%d','%s','%s','%d')"
            value=(E.getid(),E.getname(),E.getdept(),E.getsalary())
            self.cur.execute(sql % value)
            self.con.commit()
        except Exception as obj:
            print(obj)