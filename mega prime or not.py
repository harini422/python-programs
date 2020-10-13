# Finding given number is mega prime or not??
# Mega Prime -->A number is said to be megaprime if it is prime,and all its digits are also prime.

import math
n=int(input("enter ur number"))
pc=0
dc=0
x=int(math.sqrt(n))
for i in range(2,x+1):
     if n%i==0:
        print("not prime")
        break
else:
  while n:
        r=n%10
        n=n//10
        fc=0
        dc+=1
        y=int(math.sqrt(r))
        for j in range(2,y+1):
            if r%i==0:
              break
        else:
             pc+=1
  if pc==dc:
         print("mega prime")
           
  else:
      print("not a mega prime")
          
