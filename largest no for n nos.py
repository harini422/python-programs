#finding the largest number for given n no of numbers
a=[]
n=int(input("enter ur number:"))
for i in range(1,n+1):
    #print(i)
    b=int(input("enter ur number"))
    a.append(b)
a.sort()
print("largest number is",a[n-1])
