from collections import Counter


N = int(input())
A = list(map(int, input().split()))

nc = Counter(A)
C = []
for i in range(max(A) + 1):
    c = nc[i - 1] + nc[i] + nc[i + 1]
    C.append(c)

print(max(C))