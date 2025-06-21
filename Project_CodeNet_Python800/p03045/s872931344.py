from collections import deque
n , m = map(int,input().split())
route = [[] for i in range(n+1)]
for i in range(m):
    x , y , z = map(int,input().split())
    route[x].append(y)
    route[y].append(x)
    
visit = [0 for i in range(n+1)]
ans = 0
for i in range(1,n+1):
    if visit[i] == 0:
        ans += 1
        visit[i] = ans
        d = deque()
        d.append(i)
        while d:
            now = d.popleft()
            for j in route[now]:
                if visit[j] == 0:
                    visit[j] = ans
                    d.append(j)
print(max(visit))