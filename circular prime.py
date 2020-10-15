#circular prime:is a prime number with the property that the number generated at each intermediate step or all its rotations are prime numberslike--> 1193,1931,9311,3119
#eg..11,17,37,79,113,197,199

import math
def isprime(num):
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if(num%i==0):
         return False
         break
    else:
        return True
n=int(input("enter ur number:"))
temp=(n)#113
dc=len(str(n))#3
i=0
pc=0
if isprime(n):
    while True:
        r=temp%10
        temp=temp//10
        i+=1
        res=r*pow(10,dc-1)+temp
        temp=res
        if isprime(temp):
            pc+=1
        if i==dc:
            break
    if(pc==dc):
        print("circular prime")
    else:
        print("not a circular prime")
else:
    print("given input is not a prime")
         
