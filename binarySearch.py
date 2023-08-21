import array as ar
import numpy as np

n=int(input("enter the limit"))
myar=ar.array('i',[])
print("enter %d element in array"%n)
for i in range(n):
    x=int(input())
    myar.append(x)
s=int(input("enter an element for search"))

myar1=np.reshape(myar,(n))
myar1.sort()
#print(myar1)
low=0
high=n-1
f=0
while(low<=high):
    mid=(low+high)//2
    if(s==myar1[mid]):
        f=1
        break
    elif(s>myar1[mid]):
        low=mid+1
    else:
         high=mid-1
if f==1:
    print("searching success")
        
else:
     print("searching not success")  
    

#if s in myar:
  #  print("searching success")
#else:
   #print("searching not success")
        
