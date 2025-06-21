from collections import deque

n = int(input())
L = []
li = ['3', '5', '7']
que = deque(li)
while que:
    num = que.popleft()
    for i in range(3):
        nn = num + li[i]
        L.append(nn)
        if int(nn) < 10 ** 9:
            que.append(nn)
ans = 0
for num in L:
    if int(num) > n:
        break
    elif all(i in num for i in li):
        ans += 1
print(ans)
