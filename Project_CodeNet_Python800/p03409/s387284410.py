import sys
N = int(sys.stdin.readline().rstrip())

grid_r = [[0] * 2 * N for _ in range(2 * N)]

for _ in range(N):
    a, b = tuple(map(int, sys.stdin.readline().rstrip().split()))
    grid_r[a][b] = 1

b = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
b = sorted(b, key=lambda x: x[1])

ans = 0
for b_x, b_y in b:
    for x in range(b_x + 1)[::-1]:
        for y in range(b_y + 1):
            if grid_r[x][y] and (x != b_x or y != b_y):
                grid_r[x][y] = 0
                ans += 1
                break
        else:
            continue
        break
print(ans)