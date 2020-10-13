#finding given number is fully odd or even or mixed number???
n=int(input())
even_count=0
odd_count=0
dc=0
while n>0:
    r=n%10
    n=n//10
    if r%2==0:
        even_count+=1
    else:
        odd_count+=1
if even_count==0:
    print("fully odd")
elif odd_count==0:
    print("fully even")
else:
    print("mixed number")
