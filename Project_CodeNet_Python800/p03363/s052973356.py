import collections

N = int(input())
A = [0] + list(map(int, input().split()))


for i in range(1, N + 1):
    A[i] = A[i] + A[i - 1]
# print(A)

ans = 0
cnter = dict(collections.Counter(A))
for val in cnter.values():
    ans += val * (val - 1) // 2
print(ans)

