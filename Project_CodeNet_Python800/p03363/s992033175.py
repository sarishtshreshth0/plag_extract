from collections import Counter
N = int(input())
A = list(map(int, input().split()))

sa = [A[0]]
for a in A[1:]:
    sa.append(sa[-1] + a)

cnt = Counter(sa)
ans = 0
for i, j in cnt.items():
    if i == 0:
        ans += j
    ans += j * (j - 1) // 2
print(ans)