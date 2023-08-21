def even_odd(n):
    if n%2==0:
        return True
    else:
        return False

myList=[10,11,14,16,17,21,24,26]
list1=list(filter(even_odd,myList))
print(list1)
