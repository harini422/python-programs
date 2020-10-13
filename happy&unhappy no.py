# happy number is a number  which eventually reaches 1
#when replaced by the sum of the square of each digit
#eg..7 ,19 ,49,97 ,130 ,10,70
#input:n=19...output: true...19 is happy number
#1^2 + 9^2=82
#8^2 +2^2=68
#6^2 + 8^2=100
#1^2+0^2+0^2=1.....reached to 1


n=int(input("enter ur number:"))
sum1=0
while True:
    r=n%10
    n=n//10
    
    sum1=sum1+r**2
    
    if n==0:
        n=sum1
        sum1=0
        if n>=1 and n<=9:
            break
if n==1:
    print("happy numb")
else:
    print("unhappy numb")
                
                
