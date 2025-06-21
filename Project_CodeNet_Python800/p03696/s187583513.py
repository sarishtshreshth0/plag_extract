from collections import deque

N = int(input())
S = input()

s = deque(S)

ans = []
r, l, cnt = 0, 0, 0

while s:
    q = s.popleft()
    if q == ')':
        cnt -= 1
        if cnt < 0:
            l += 1
            cnt += 1
    else:
        cnt += 1
        
if cnt > 0: r += cnt

print('('*l + S + ')'*r)