import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, D = map(int, input().split())
points = []
for _ in range(N):
    point = list(map(int, input().split()))
    points.append(point)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        dis = 0
        for y, z in zip(points[i], points[j]):
            dis += (y - z) ** 2
        dis = dis ** 0.5
        if dis.is_integer():
            ans += 1
print(ans)