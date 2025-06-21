import math
from collections import defaultdict,deque
#from itertools import permutations
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

n=ii()
s=ip()
ans=1
for i in range(1,n):
    if(s[i]!=s[i-1]):
        ans+=1
print(ans)        