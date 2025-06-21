N = int(input())
A = list(map(int, input().split()))

res = {}
for i in range(-1, 10**5+1):
    res[i] = 0

for ai in A:
    for i in [ai-1, ai, ai+1]:
        res[i] += 1

print(max(res.values()))
