from collections import Counter
n = int(input())
a = list(map(int, input().split()))
A = Counter(a)
ans = 0
for x,y in A.items():
    z = y + A[x-1] + A[x+1]
    ans = max(z, ans)
print(ans)