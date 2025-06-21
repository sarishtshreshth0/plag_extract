"Zero-Sum Ranges"
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cum_sum = [A[0]]
for a in A[1:]:
    cum_sum.append(cum_sum[-1]+a)
count = Counter(cum_sum)
ans = 0
for k, v in count.items():
    ans += v * (v-1) // 2
print(ans + count[0])
