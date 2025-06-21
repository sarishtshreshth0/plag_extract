from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

sum = [0]
for i in range(N):
    sum.append(sum[i] + A[i])

sum.sort()
dict = defaultdict(int)
for i in range(N + 1):
    dict[sum[i]] += 1

ans = 0
for key, val in dict.items():
    ans += val * (val - 1) // 2

print(ans)
