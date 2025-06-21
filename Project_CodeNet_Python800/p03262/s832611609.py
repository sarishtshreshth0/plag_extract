from math import gcd as g
n,x=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
if x<=l[0]:
    l.insert(0,x)
elif x>=l[-1]:
    l.append(x)
else:
    for i in range(n-1):
        if l[i]<=x<l[i+1]:
            l.insert(i+1,x)
            break
ans=0
for i in range(n):
    ans=g(ans,l[i+1]-l[i])
print(ans)
    
    
    
