from itertools import *
N = int(input())
S = []
ans = 0

for n in range(10):
  S+=list(product("357",repeat=n))

for s in S:
  if len(set(s))==3 and int("".join(s))<=N:
    ans+=1

print(ans)