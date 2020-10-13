#Palindromic number is a number that remains the same when its digits are reversed.
n=int(input("enter ur num:"))
rev=0
temp=n
while True:
    r=n%10
    n=n//10
    rev=rev*10+r
    if n==0:
        break
if temp==rev:
    print("palindrome")
else:
    print("not palimdrome")
