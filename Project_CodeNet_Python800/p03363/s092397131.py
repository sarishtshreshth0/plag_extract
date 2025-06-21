from collections import defaultdict

N = int(input())
A = [int(i) for i in input().split()]

cumsum = [0]
for v in A:
    cumsum.append(cumsum[-1]+v)

counter = defaultdict(lambda: 0)
for v in cumsum:
    counter[v] += 1

res = 0
for _, v in counter.items():
    res += (v*(v-1))//2

print(res)