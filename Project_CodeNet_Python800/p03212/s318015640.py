from collections import deque

n = int(input())

d = deque([3, 5, 7])
res = 0
while True:
    v = d.popleft()
    if v > n:
        break
    if len(set(str(v))) == 3:
        res += 1
    d.append(v * 10 + 3)
    d.append(v * 10 + 5)
    d.append(v * 10 + 7)

print(res)