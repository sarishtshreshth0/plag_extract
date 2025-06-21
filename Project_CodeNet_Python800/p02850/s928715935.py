n = int(input())
L = []
d = {}
for _ in range(n-1):
    a, b = map(int, input().split())
    L.append((a, b))
    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)
k = 0
for i in d.keys():
    tmp_k = len(d[i]) if i == 1 else len(d[i]) + 1
    k = max(k, tmp_k)
print(k)
key = sorted(d.keys())
dd = {1: 0}
ans = {}
for i in key:
    v = d[i]
    cnt = 1
    for j in v:
        if cnt != dd[i]:
            c = cnt
            cnt += 1
        else:
            c = cnt + 1
            cnt += 2
        ans[(i, j)] = c
        dd[j] = c
for a, b in L:
    print(ans[(a, b)])
