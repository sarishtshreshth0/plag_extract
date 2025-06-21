from math import gcd

N, X = map(int, input().split())
xs = sorted(map(int, input().split()))
ds = [xs[i] - X for i in range(N)]
ans = abs(ds[0])
for d in ds:
    ans = gcd(abs(d), ans)
print(ans)