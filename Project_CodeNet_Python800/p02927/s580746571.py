M, D = map(int, input().split())


def isSEKIDay(m, d):
    ds = str(d).zfill(2)
    d1 = int(ds[1])
    d10 = int(ds[0])
    return (d1 >= 2) and (d10 >= 2) and (d1 * d10 == m)


cnt = 0
for i in range(M):
    for j in range(D):
        if isSEKIDay(i + 1, j + 1):
            cnt += 1

print(cnt)
