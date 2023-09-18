import MySQLdb


class MyConnection:
    @staticmethod
    def getConnection():
        con = MySQLdb.Connect(host="localhost", user="root", password="root", database="pythondb")
        return con
