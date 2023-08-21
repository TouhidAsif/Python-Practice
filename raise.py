a=int(input("enter first value"))
b=int(input("enter second value"))
try:
    if(b==5):
        raise ZeroDivisionError("Divide by 5 Error")
    c=a//b
    print("Division is",c)
except ZeroDivisionError as msg:
    print(msg)
