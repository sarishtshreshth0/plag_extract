from collections import deque
n = int(input())

que = deque(['7','5','3'])
semi = []

while que:
    x = que.popleft()
    if int(x) <= n:
        semi.append(x)
        for new_x in [x+c for c in ['7','5','3']]:
            que.append(new_x)

cnt = 0
for i in semi:
    if all(i.count(c)>0 for c in ['7','5','3']):
        cnt += 1
print(cnt)