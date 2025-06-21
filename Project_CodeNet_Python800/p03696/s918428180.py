n = int(input())
s = str(input())
c = 0
from collections import deque
res = deque([])
for i in range(n):
    if s[i] =='(':
        c += 1
    else:
        c -= 1
    if c < 0:
        res.appendleft('(')
        c = 0
    res.append(s[i])
if c > 0:
    res.append(')'*c)
print(''.join(list(res)))
