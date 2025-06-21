N = int(input())
R = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]
R = sorted(R)
B = sorted(B)

res = 0
for bx, by in B:
    idx = -1
    tmp = -1
    for i, (rx, ry) in enumerate(R):
        if rx < bx and ry < by:
            if ry >= tmp:
                tmp = ry
                idx = i
    if idx != -1:
        R.pop(idx)
        res += 1
print(res)