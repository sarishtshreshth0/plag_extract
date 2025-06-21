n = int(input())
lst = list(map(int, input().split()))
res = 10 ** 10
for i in range(1, n):
  res = min(res, abs(sum(lst[:i]) - sum(lst[i:])))
print(res)