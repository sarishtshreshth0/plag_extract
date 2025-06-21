from collections import defaultdict,deque
n = int(input())
d = defaultdict(list)
l = []
for i in range(n-1):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
    l.append((a,b))

# print(d)

que = deque([a])
visited = [-1] + [False]*n
visited[a] = True

preans = defaultdict(list)
ans = defaultdict(int)
maxi = 1

while que:
    v = que.popleft()
    cnt = 1
    for x in d[v]:
        if not visited[x]:
            while cnt in preans[v]:
                cnt += 1
            maxi = max(maxi,cnt)
            preans[x].append(cnt)
            ans[(v,x)] = cnt
            ans[(x,v)] = cnt
            que.append(x)
            visited[x] = True
            cnt += 1
    # print(preans)
    # print(ans)
print(maxi)

for i in l:
    print(ans[i])