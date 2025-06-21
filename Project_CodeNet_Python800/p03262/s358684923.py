n,k=list(map(int,input().split()))
x=list(map(int,input().split()))
p=[]
for i in range(n):
  p.append(abs(x[i]-k))
ans=0
import math
for i in p:
  ans=math.gcd(ans,i)
print(ans)
