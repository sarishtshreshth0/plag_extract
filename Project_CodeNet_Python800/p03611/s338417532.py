n=int(input())
L=list(map(int,input().split()))

import collections

d=collections.Counter(L)
S=d[0]+d[1]
for i in range(1, 10**5+1):
	s=d[i-1]+d[i]+d[i+1]
	S=max(S,s)
print(S)