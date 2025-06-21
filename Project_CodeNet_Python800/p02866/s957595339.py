N = int(input())
D = list(map(int, input().split()))
MOD = 998244353

#以下が an mod p を求めるソースコードです.
def power_func(a, n, p):
    res = 1 #これは答え
    while n > 0:
        if n & 1:
            res = res * a % p
        a = a * a % p #1が立っているかどうかに関わらず次のaの累乗を用意しておく
        n = n >> 1
    return res

bucket = [0] * (max(D) + 1)
for dist in D:
    bucket[dist] += 1
# print(bucket)

if bucket[0] != 1 or D[0] != 0:
    print(0)
else:
    ans = 1
    for i in range(len(bucket) - 1):
        ans = (ans * power_func(bucket[i], bucket[i + 1], MOD)) % MOD
    print(ans)
