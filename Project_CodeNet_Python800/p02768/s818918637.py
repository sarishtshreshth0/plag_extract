n,a,b=map(int,input().split())
x=pow(2,n,10**9+7)
s=1
for i in range(a):
    s=s*(n-i)*pow((1+i),10**9+5,10**9+7)
    s=s%(10**9+7)
t=1
for i in range(b):
    t=t*(n-i)*pow((1+i),10**9+5,10**9+7)
    t=t%(10**9+7)
ans=(x-s-t-1)%(10**9+7)
print(ans)