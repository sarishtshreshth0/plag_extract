import sys
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n)]
ans = [0] * (n-1)

for i in range(n-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append([b, i])

# coloring
def dfs(now, color):
    cnt = 1
    for to, num in graph[now]:
        if cnt == color:
            cnt += 1
        ans[num] = cnt
        dfs(to, cnt)
        cnt += 1    

dfs(0, 0)

print(max(ans))
for i in ans:
    print(i)