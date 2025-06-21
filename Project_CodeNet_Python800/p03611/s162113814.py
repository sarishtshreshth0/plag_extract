n = int(input())
A = tuple(map(int, input().split()))
from collections import Counter
CA = Counter(A)

mc = 0
for x in range(1, 10**5):
    mc = max(mc, CA[x-1] + CA[x] + CA[x+1])
print(mc)