"""ABC091 2D Plane 2N Points diff:
"""

N = int(input())

ab = [tuple(map(int, input().split())) for _ in range(N)]
cd = [tuple(map(int, input().split())) for _ in range(N)]

ans_x = 0
cd.sort(key=lambda x: x[0])
ab.sort(key=lambda x: x[1], reverse=True)
ab_used = [0]*N
for i, (c, d) in enumerate(cd):
    for j, (a, b) in enumerate(ab):
        if not ab_used[j] and a < c and b < d:
            ab_used[j] = 1
            ans_x += 1
            break

ans_y = 0
cd.sort(key=lambda x: x[1])
ab.sort(key=lambda x: x[0], reverse=True)
ab_used = [0]*N
for i, (c, d) in enumerate(cd):
    for j, (a, b) in enumerate(ab):
        if not ab_used[j] and a < c and b < d:
            ab_used[j] = 1
            ans_y += 1
            break

print(max(ans_x, ans_y))