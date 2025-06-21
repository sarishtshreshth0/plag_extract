import itertools

n = int(input())
A = [0]+list(map(int,input().split()))

cumsum = list(itertools.accumulate(A))

d = {}

ans = 0
for i in cumsum:
    if i not in d:
        d[i] = 1
    else:
        ans += d[i]
        d[i] += 1

print(ans)