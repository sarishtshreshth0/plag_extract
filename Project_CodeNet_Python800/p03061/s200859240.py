from fractions import gcd
import numpy as np
n=int(input())
data=list(map(int,input().split()))
left=np.zeros(n+1,dtype=np.int)
right=np.zeros(n+1,dtype=np.int)
kotae=1
for i in range(n):
    left[i+1]=gcd(left[i],data[i])
    right[n-i-1]=gcd(right[n-i],data[n-i-1])
for j in range(n):
    num=gcd(left[j],right[j+1])
    kotae=max(num,kotae)
print(kotae)