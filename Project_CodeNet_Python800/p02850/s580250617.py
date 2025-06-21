from collections import deque
n = int(input())
zyun = []
route = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    zyun.append([a,b])
    route[a].append(b)
iro = [0 for i in range(n+1)]
ans = {}
q = deque()
q.append(1)
while q:
    now = q.popleft()
    cou = 1
    for k in route[now]:
        if iro[now] == cou:
            cou += 1
        ans[str(now) + "+" + str(k)] = cou
        iro[k] = cou
        q.append(k)
        cou += 1
print(max(iro))
for i,j in zyun:
    print(ans[str(i)+"+"+str(j)])