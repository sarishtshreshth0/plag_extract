# AtCoder Beginner Contest 091
# C - 2D Plane 2N Points
# https://atcoder.jp/contests/abc091/tasks/arc092_a

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x: x[0])
B.sort(key=lambda x: x[0])

used = [False]*N

cnt = 0
for u, v in B:
    maxy = -1
    maxi = -1

    for i, (x, y) in enumerate(A):

        if x >= u:
            break
        if used[i] or y >= v:
            continue

        if maxy < y:
            maxy = y
            maxi = i

    if maxy > -1:
        used[maxi] = True
        cnt += 1

print(cnt)
