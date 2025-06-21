N = int(input())
ds = set()
m = 1
while m*m <= N:
    if N%m==0:
        ds.add(m)
        ds.add(N//m)
    m += 1

ans = 999
for d in ds:
    e = N//d
    t = max(len(str(d)) ,len(str(e)))
    ans = min(ans, t)
print(ans)