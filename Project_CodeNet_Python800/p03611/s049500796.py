from collections import Counter

n = int(input())
l = list(map(int, input().split()))
c = Counter(l)
s = set(l)
ans = 0

for i in s:
    ans = max(c[i-1] + c[i] + c[i+1], ans)
print(ans)
