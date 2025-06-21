N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]

A.sort()
B.sort()

cnt = 0
for u, v in B:
    maxy = -1
    maxi = -1

    for i, (x, y) in enumerate(A):

        if x >= u:
            break
        if y >= v:
            continue

        if maxy < y:
            maxy = y
            maxi = i

    if maxy > -1:
        A.pop(maxi)
        cnt += 1

print(cnt)
