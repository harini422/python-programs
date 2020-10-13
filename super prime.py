# Finding given number is super prime or not???
#super prime numbers are the subsequence of prime numbers that occupy prime numbered positionswithin the sequence of all prime numbers
#super prime-- 2 3 5 7 11 13 17 19
               #1 2 3 4  5  6  7  8
import math
n=int(input())
def is_prime(n):
  if n==1:
      return False
  else:
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
    else:
         return True
        
def position_prime(n):
    position=0
    for i in range(1,n+1):
      if is_prime(i):
         position+=1
    return position
    
if is_prime(n):
    if is_prime(position_prime(n)):
        print("super prime")
    else:
        print("not a  super prime")
else:
    print("not a prime")
        
