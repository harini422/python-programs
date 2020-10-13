#strong number  means factors of individal number adding is equal to the given number
n=int(input("enter ur number:"))
sum=0
temp=n
while n:
    r=n%10#5,4,1
    n=n//10#14,1,0
    fc=1
    for i in range(1,r+1):
        fc=fc*i#1*2=2*3=6*4=24*5=12--#r=4--24#r=1--1
    
    sum=sum+fc#0+120=120+24+1=145
if(sum==temp):#145=145
    print("strong numb")
else:
    print("not strong numb")
      
