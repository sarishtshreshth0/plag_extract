import sys,collections,math
input = sys.stdin.readline

n,a,b = list(map(int,input().split()))
m = 10**9+7
ans = pow(2,n,m)


la  = 1
laa = 1
for i in range(n,n-a,-1):
    la = (la*i)%m
for i in range(1,a+1):
    laa = (laa*i)%m

lb  = 1
lbb = 1
for i in range(n,n-b,-1):
    lb = (lb*i)%m
for i in range(1,b+1):
    lbb = (lbb*i)%m

la = (la*pow(laa,10**9+5,m))%m
lb = (lb*pow(lbb,10**9+5,m))%m

print((ans-la-lb-1)%m)
