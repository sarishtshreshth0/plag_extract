n, m = map(int, input().split())
x = list(map(int, input().split()))

if n >= m:
    print(0)
else:
    x.sort()
    diffs = []
    for i in range(m - 1):
        diffs.append((x[i+1] - x[i], i))
    diffs.sort(reverse=True)
    diffs = diffs[:n-1]

    idxs = sorted([0] + [diff[1] + 1 for diff in diffs], reverse=True)

    ans = 0
    pos = -1
    for i in range(m):
        if idxs and i == idxs[-1]:
            pos = x[idxs.pop()]
        else:
            ans += x[i] - pos
            pos = x[i]
    print(ans)
