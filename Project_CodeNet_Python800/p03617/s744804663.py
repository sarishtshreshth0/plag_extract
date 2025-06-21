*aa,n = map(int, open(0).read().split())

n *= 1000

bb = [250,500,1000,2000]

for i in range(1,4):
    aa[i] = min(aa[i], aa[i-1]*2)

ans = 0
for b,a in zip(bb[::-1], aa[::-1]):
    ans += n // b * a
    n %= b

print(ans)