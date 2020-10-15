#A number is a Spy number ,if sum and product of all digits are equal.
#eg:123-->sum of its digit is 6 (1+2+3=6) and 
          #product of its digits is 6(1*2*3=6)

n=int(input())
sum=0
product=1

while True:
    r=n%10
    n=n//10
    sum=sum+r
    product=product*r
    if n==0:
        break
if sum==product:
    print("spy number")
else:
    print("not spy number")
