mod = 998244353
n = int(input())
d = list(map(int, input().split()))

if d[0] != 0:
    print(0)
    exit(0)

max_d = max(d)
cnt = [0] * (max_d + 1)

for num in d:
    cnt[num] += 1

if cnt[0] > 1:
    print(0)
    exit(0)

ans = 1

for i in range(1, len(cnt)):
    ans *= pow(cnt[i - 1], cnt[i], mod)
    ans %= mod

print(ans)
