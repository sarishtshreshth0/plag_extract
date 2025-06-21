from collections import Counter
n=int(input())
a=list(map(int,input().split()))
s=[0]*(n+1)

for i in range(n):
    s[i+1]=s[i]+a[i]
c=Counter(s)
ans=0
for b in c.items():
    k=b[0]
    i=b[1]
    if k==0:
        ans+=i-1
        if i>2:
            ans+=(i-1)*(i-2)//2
    elif i>1:
        ans+=i*(i-1)//2
print(ans)