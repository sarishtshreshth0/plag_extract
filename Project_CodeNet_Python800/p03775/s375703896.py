n=int(input())
def g(x):
    z=0
    while x>=1:
        z+=1
        x=x//10
    return z
def f(a,b):
    return max(g(a),g(b))
i=1
ans=10**10
while i*i<=n:
    if n%i==0:
        ans=min(ans,f(i,n//i))
    i+=1
print(ans)
