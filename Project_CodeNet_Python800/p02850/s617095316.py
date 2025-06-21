from collections import deque
n = int(input())
k = 0
data = [[] for _ in range(n)]
ans_index = []

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    data[a].append(b)
    ans_index.append(b)

q = deque([0])
color = [0] * n
while q:
    cur = q.popleft()
    c = 1
    for x in data[cur]:
        if c == color[cur]:
            c += 1
    
        color[x] = c
        c += 1
        q.append(x)

print(max(color))
for i in ans_index:
    print(color[i])
