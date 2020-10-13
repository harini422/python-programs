#Finding factorial for given number
def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)
        print(num)
num=int(input("enter ur num"))
if num<0:
    print("factorial cannot find for negative num")
elif num==0:
    print("factorial of 0 is 1")
else:
    print("factorial of",num,"is:",factorial(num))
