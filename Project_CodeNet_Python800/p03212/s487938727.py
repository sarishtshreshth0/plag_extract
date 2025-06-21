from collections import deque

n = int(input())
q = deque(['3','5','7'])
ans = 0
l = []
while True:
    v = q.popleft()
    if int(v) >= n:
        if int(v) == n and ('3' in v and '5' in v and '7' in v):
            ans += 1
        print(ans)
        exit() 
    if '3' in v and '5' in v and '7' in v:
        ans += 1
        l.append(int(v))
    q.append(v+'3')
    q.append(v+'5')
    q.append(v+'7')