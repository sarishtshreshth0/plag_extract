from math import sqrt
n, d = map(int, input().split())

vs = []
for i in range(n):
    v = list(map(int, input().split()))
    vs.append(v)


def ds(a, b):
    s = 0
    for i in range(d):
        s += (b[i] - a[i])**2
    return sqrt(s)


ans = 0
for i in range(n):
    for j in range(i+1, n):
        dist = ds(vs[i], vs[j])
        if dist == int(dist):
            ans += 1

print(ans)
