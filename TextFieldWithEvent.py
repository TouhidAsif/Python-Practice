from tkinter import *


class MyEntry:
    def __init__(self,myroot):
        self.mf = Frame(myroot, width=500, height=500, bg='gray')
        self.mf.pack()
        self.mf.propagate(0)
        self.lb1 = Label(self.mf, text="Enter a String:", font=('Arial', 10, 'bold'))
        self.lb1.place(x=50, y=100)


myroot = Tk()
myroot.geometry("500x500")
myroot.maxsize(700, 700)
myroot.minsize(400, 400)
myroot.title("Entry demo data")
M1=MyEntry(myroot)
myroot.mainloop()
