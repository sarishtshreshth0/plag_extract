from collections import deque

N = int(input())

data = [[] for i in range(N)]


for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    data[a].append((i,b))###(edge no.,edgeの行き先)
    data[b].append((i,a))###(edge no.,edgeの行き先)

l = 0

for i in range(N):
    l = max(l,len(data[i]))

print(l)

stack = deque([(0,-1)]) ###(頂点番号, 前の頂点からきた色)
visit = [0]*N
visit[0] = 1
color = [0]*(N-1)

while stack:
    x = stack.pop()
    c = 1
    for y in data[x[0]]:
        if visit[y[1]] == 1:
            continue
        else:
            visit[y[1]] = 1
            if c != x[1]:
                color[y[0]]=c
                stack.append((y[1],c))
                c += 1
            else:
                color[y[0]]=c+1
                stack.append((y[1],c+1))
                c += 2

#print(color)
for i in range(N-1):
    print(color[i])