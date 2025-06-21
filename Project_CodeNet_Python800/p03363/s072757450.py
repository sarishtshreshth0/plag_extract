from collections import Counter

N, *A = map(int, open(0).read().split())

s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + A[i]
    
ctr = Counter(s[1:])
ans = ctr[0]
for v in ctr.values():
    ans += v * (v - 1) // 2
print(ans)
