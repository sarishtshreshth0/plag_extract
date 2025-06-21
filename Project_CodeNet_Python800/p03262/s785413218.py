from math import gcd
n,x=map(int,input().split())
lst=list(map(int,input().split()))

for i in range(n):
    lst[i]=abs(x-lst[i])

a=lst[0]
for i in range(1,n):
    a=gcd(a,lst[i])

print(a)