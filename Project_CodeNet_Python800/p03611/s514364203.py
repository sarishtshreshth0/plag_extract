from collections import Counter

n = int(input())
A = [int(i) for i in input().split()]
counts = Counter(A)

ans = 0
for k, v in counts.items():
    tmp = v
    if k + 1 in counts.keys():
        tmp += counts[k + 1]
    if k - 1 in counts.keys():
        tmp += counts[k - 1]
    ans = max(tmp, ans)

print(ans)
