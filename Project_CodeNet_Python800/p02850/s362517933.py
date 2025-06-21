N = int(input())
query = [[] for _ in range(N)]
color = []
m = [0]*N
for n in range(N-1):
    a, b = map(int, input().split())
    query[a-1].append(b-1) 
    query[b-1].append(a-1)
    color.append((min(a, b), max(a, b)))
    m[a-1] += 1
    m[b-1] += 1

print(max(m))
from collections import deque
queue = deque()
queue.appendleft(0)
checked = [-1]*N
checked[0] = 0
dic = {}
while queue:
    v = queue.pop()
    oya = checked[v]
    lis = query[v]
    cnt = 1
    for i in lis:
        if checked[i]!=-1:
            continue
        if cnt==oya:
            cnt += 1
        queue.appendleft(i)
        dic[(min(v+1, i+1), max(v+1, i+1))] = cnt
        checked[i] = cnt
        cnt += 1

for n in range(N-1):
    a, b = color[n]
    print(dic[(min(a, b), max(a, b))])