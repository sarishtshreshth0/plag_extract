N = int(input())
deg = [0 for _ in range(N)]
edges = [[] for _ in range(N - 1)]
a = []
for i in range(N - 1):
    in1, in2 = map(int, input().split())
    a.append([in1, in2, i])
a = sorted(a, key = lambda x: x[0])
for i in range(N - 1):
    edges[i] = [a[i][0] - 1, a[i][1] - 1, a[i][2]]
    deg[a[i][0] - 1] += 1
    deg[a[i][1] - 1] += 1
deg_max = max(deg)
print(deg_max)

co = [0 for _ in range(N)]
ans = [0 for _ in range(N - 1)]
for i in range(N - 1):
    a = edges[i][0]
    b = edges[i][1]
    temp = 1 + (co[a] % deg_max)
    co[a] = temp
    co[b] = temp
    ans[edges[i][2]] = temp
for i in range(N - 1):  print(ans[i])