n=int(input("enter limit"))
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print("*",end="")
        #print("%d"%i,end="")
    print()

n=int(input("enter limit"))
for i in range(1,n+1,1):
    for j in range(n,i-1,-1):
        print("*",end="")
        #print("%d"%i,end="")
    print()
        
