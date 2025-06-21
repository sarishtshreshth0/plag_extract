from itertools import accumulate
from collections import Counter

n = int(input())
A = [0] + list(map(int, input().split()))
ans = 0
SA = list(accumulate(A))
# print(SA)
CSA = Counter(SA[1:])
# print(CSA)
for i, num in CSA.items():
    if i == 0:
        ans += num
    ans += num * (num - 1) // 2

# for i in range(n):
#     for j in range(i + 1, n + 1):
#         goukei = SA[i] - SA[j]
#         print(goukei)
#         if goukei == 0:
#             ans += 1
print(ans)
