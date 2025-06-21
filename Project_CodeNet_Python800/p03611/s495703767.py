from collections import Counter

n = int(input())
A = Counter(sorted(list(map(int, input().split()))))

ans = 0
for k, v in A.items():
    ans = max(v+A[k-1]+A[k+1], ans)
print(ans)