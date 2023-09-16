from tkinter import *
myroot=Tk()
myroot.geometry('600x600')
myroot.maxsize(600,600)
myroot.minsize(600,600)
myroot.title("Employee Registration Form")


lb1=Label(text="Enter Employee Id")
lb1.grid(row=0,column=0)
userid=IntVar()
txtid=Entry(textvariable=userid)
txtid.grid(row=0,column=2)



myroot.mainloop()