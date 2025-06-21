from collections import Counter

N = int(input())
D = list(map(int, input().split()))
c = Counter(D)

# 根は0である必要がある。
if D[0] != 0:
    print(0)
    exit(0)
# 0が1つでない場合の答えは0になる
if c[0] != 1:
    print(0)
    exit(0)

MOD = 998244353
cnt = 1
for i in range(1, max(D)+1):
    cnt *= pow(c[i-1], c[i], MOD)
print(cnt % MOD)
