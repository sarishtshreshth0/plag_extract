n = int(input())
A = list(map(int, input().split()))
acc = [0] * (n + 1)
for i in range(n):
    acc[i + 1] = acc[i] + A[i]

from collections import Counter

cnt = 0
cacc = Counter(acc)
for k, v in cacc.items():
    if v > 1:
        cnt += v * (v - 1) // 2
print(cnt)