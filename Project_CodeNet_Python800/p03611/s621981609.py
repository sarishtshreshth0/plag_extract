from collections import Counter
n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ans = 0
start, end = min(A), max(A) + 1
for v in range(start, end):
    ans = max(C[v - 1] + C[v] + C[v + 1], ans)
print(ans)