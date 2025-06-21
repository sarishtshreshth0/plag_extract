import collections
N = int(input())
D = list(map(int, input().split()))
d = collections.Counter(D)
maxnum = max(D)
ans = 1
for i in range(maxnum+1):
    if i == 0:
        if D[0] != 0 or d.get(0,0) != 1:
            ans = 0
            break
    else:
        if d.get(i, 0) == 0:
            ans = 0
            break
        ans *= d[i-1]**d[i]

print(ans%998244353)