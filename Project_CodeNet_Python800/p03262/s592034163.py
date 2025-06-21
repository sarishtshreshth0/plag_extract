def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
N,X=map(int,input().split())
x=list(map(int,input().split()))
kari=[]
for i in range(N):
    kari.append(abs(x[i]-X))
ans=gcd(min(kari),max(kari))
for i in range(N):
    ans=gcd(ans,kari[i])
print(ans)