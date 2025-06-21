from collections import Counter

n = int(input())
A = list(map(int, input().split()))

S = [0] * (n + 1)
for i in range(1, n + 1):
    S[i] = S[i - 1] + A[i - 1]
counter = Counter(S)
result = 0
for k in counter.keys():
    if counter[k] <= 1:
        continue
    result += (counter[k] - 1 + 1) * (counter[k] - 1) // 2
print(result)
