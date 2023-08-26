from tkinter import *


class MyEntry:
    def __init__(self,myroot):
        self.mf = Frame(myroot, width=500, height=500, bg='gray')
        self.mf.pack()
        self.mf.propagate(0)
        self.lb1 = Label(self.mf, text="Enter a String:", font=('Arial', 10, 'bold'))
        self.lb1.place(x=50, y=100)
        self.strv = StringVar()
        self.txt1 = Entry(self.mf, font=('Arial', 13, 'bold'), fg='red', textvariable=self.strv)
        self.txt1.place(x=150, y=100)
        self.txt1.bind('<Return>', self.display)
        self.btn1 = Button(self.mf, text="click here", font=('Arial', 10, 'bold'), command=lambda: self.display(0))
        self.btn1.place(x=50, y=200)
        self.lb2 = Label(self.mf, text="-", font=('Arial', 10, 'bold'))
        self.lb2.place(x=200, y=200)

    def display(self, event):
        s = self.strv.get()
        self.lb2["text"] = s.upper()


myroot = Tk()
myroot.geometry("500x500")
myroot.maxsize(700, 700)
myroot.minsize(400, 400)
myroot.title("Entry demo data")
M1=MyEntry(myroot)
myroot.mainloop()
