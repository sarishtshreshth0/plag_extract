n = int(input())
a = list(map(int, input().split()))
from collections import Counter
c = Counter(a)
ans = 0
for i in c:
    if ans < c[i] + c[i - 1] + c[i + 1]:
        ans = c[i] + c[i - 1] + c[i + 1]
print(ans)