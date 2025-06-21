N = int(input())
red = [tuple(map(int, input().split())) for _ in range(N)]
blue = [tuple(map(int, input().split())) for _ in range(N)]

red.sort(reverse=True)

cnt = 0
track = [0] * N
for r in red:
    y = 2 * N + 1
    p = -1
    for i, b in enumerate(blue):
        if track[i] == 0:
            if b[0] > r[0] and b[1] > r[1] and b[1] < y:
                y = b[1]
                p = i
    if p >= 0:
        track[p] = 1
        cnt += 1

print(cnt)
