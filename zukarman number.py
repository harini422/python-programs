#zukarman number is a number which is divisible by the product of its individual digits
#input-->n=115
#1*1*5=5 and 115%5==0

def is_zukarman(n):
    product=1
    temp=n
    while n:
        r=n%10
        n=n//10
        product=product*r
    if temp% product==0:

        return True
    return False
n=int(input())
print(is_zukarman(n))

