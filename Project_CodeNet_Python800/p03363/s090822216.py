from collections import Counter

n = int(input())
A = list(map(int, input().split()))
cum_sum = [0] * (n+1)
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + A[i]
C = Counter(cum_sum[1:])
ans = 0
for k, v in C.items():
    if k == 0:
        ans += v + (v*(v-1)//2)
    else:
        ans += (v*(v-1)//2)
print(ans)
