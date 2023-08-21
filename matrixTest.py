import numpy as np
import array as ar

m,n=[int(a) for a in input("enter value of row and column").split()]
x=m*n
myar1=ar.array('i',[])
print("enter %d element of matrix "%x)
for i in range(x):
    b=int(input())
    myar1.append(b)
myar2=np.reshape(myar1,(m,n))
print(myar2)
