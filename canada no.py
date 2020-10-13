# finding given number is canada number or not

#  Canada number is a number n such that the sum of the squares of the digiits of n is equal to
#the sum of the non trival division of  n(sum of division of n)
#eg:125 1^2+2^2+5^2=30 and 5,25=30 equal
from math import sqrt
def sqrsum_of_digit(n):
#n=int(input())
  sum1=0
  while n:
     r=n%10
     n=n//10
     sum1=sum1+r**2     
  return sum1
  
def non_trival_divisiors(n):
    result=0
    for i in range(1,int(sqrt(n))+1):
      if n%i==0:
        if i==n//i:
           result+=i
        else:
            result+=i+n//i
            
    return result-1-n 

    
def is_canada(n):
     if sqrsum_of_digit(n)==non_trival_divisiors(n):
         return True
     return False
n=int(input("enter ur number:"))
print(is_canada(n))
            
            
    
