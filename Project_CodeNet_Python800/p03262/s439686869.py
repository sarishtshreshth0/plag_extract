import math 
import fractions

a,b=map(int,input().split())
l=list(map(int,input().split()))
b_l = []
for i in range(a):
    b_l.append(abs(b-l[i]))
ans=b_l[0]
for j in range(1,a):
    ans = fractions.gcd(ans,b_l[j])
print(ans)
