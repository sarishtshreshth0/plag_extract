N = int(input())
xs = []
ys = []

for _ in range(N):
    a, b = map(int, input().split())
    xs.append((a, b))
xs.sort(key=lambda l: l[0])

for _ in range(N):
    c, d = map(int, input().split())
    ys.append((c, d))
ys.sort(key=lambda l: l[0])

used = []
ret = 0
for (c, d) in ys:
    l = []
    for (a, b) in xs:
        if a < c and b < d:
            l.append((a, b))

    ab = None
    for (a, b) in l:
        if used.count((a, b)) == 1:
            continue
        if ab is None:
            ab = (a, b)
        elif ab[1] < b:
            ab = (a, b)

    if ab is not None:
        used.append(ab)
        ret += 1

print(ret)
