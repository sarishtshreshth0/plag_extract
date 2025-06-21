#Harshad Number
n=int(input())
fx=0
x=n
while x>0:
    fx+=x%10
    x=x//10

if n%fx==0:
    print("Yes")
    #print(fx)
else:
    print("No")
    #print(fx)

