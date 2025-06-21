from collections import Counter

N = [int(_) for _ in input().split()][0]
a = [int(_) for _ in input().split()]
s = [0] * (N + 1)

cnt = Counter()
for i in range(N):
    s[i + 1] = a[i] + s[i]
    cnt[s[i + 1]] += 1

ans = 0
for k, v in cnt.items():
    # print(k,v)
    if v <= 1: continue

    ans += (v * (v - 1)) // 2
ans += cnt[0]
print(ans)
