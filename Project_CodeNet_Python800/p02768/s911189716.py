n,a,b=map(int,input().split())
num9=10**9+7
num2=pow(2,n,num9)-1
def cul(num1,num2):
    num=1
    for i in range(num1-num2+1,n+1):
        num*=i
        num%=num9
    for i in range(1,num2+1):
        num*=pow(i,num9-2,num9)
        num%=num9
    return num
print((num2-cul(n,a)-cul(n,b))%num9)
