from collections import deque
from fractions import gcd
n = int(input())
a = list(map(int,input().split()))
l = a[0]
r = a[-1]
ll = deque([l])
rl = deque([r])
for i in range(1,n-1):
    l = gcd(l,a[i])
    r = gcd(r,a[-(i+1)])
    ll.append(l)
    rl.appendleft(r)

llas = ll.pop()
rlas = rl.popleft()

res = max(llas,rlas)
for i in range(n-2):
    res = max(res, gcd(ll.pop(), rl.pop()))
print(res)
