MOD=10**9+7

def powmod(a,n,m): #a^n mod m
    ans=1
    while n!=0:
        if n&1: ans=ans*a%m
        a=a*a%m
        n>>=1
    return ans%m

def fact(a,b):
    ans=1
    for i in range(a,b+1): ans=ans*i%MOD
    return ans

n,a,b=map(int,input().split())

ans=powmod(2,n,MOD)-1
ta1=fact(n-a+1,n)
tb1=fact(n-b+1,n)
ta2=pow(fact(1,a),MOD-2,MOD)
tb2=pow(fact(1,b),MOD-2,MOD)
a=ta1*ta2%MOD
b=tb1*tb2%MOD
print((ans-a-b)%MOD)