import collections
N = int(input())
D = list(map(int,input().split()))

if D[0] != 0 or 0 in D[1:]:
    print(0)
    exit()

A = collections.Counter(D)
A = list(A.items())
A.sort()

if len(A) != max(D) + 1:
    print(0)
    exit()

ans = 1
for i in range(max(D)):
    ans *= A[i][1]**A[i+1][1]
    if ans >= 998244353:
        ans %= 998244353
print(ans)