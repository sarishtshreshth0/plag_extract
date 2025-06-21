import math
import fractions
n=int(input())
a=list(map(int,input().split()))
left=[0]*(n+1)
right=[0]*(n+1)
left[1]=a[0]
right[1]=a[n-1]
for i in range(2,n+1):
    left[i]=fractions.gcd(left[i-1],a[i-1])
    right[i]=fractions.gcd(right[i-1],a[n-i])
ans=0
for i in range(1,n-1):
    ans=max(ans,fractions.gcd(left[i],right[n-1-i]))
print(max(ans,right[n-1],left[n-1]))
