from collections import Counter

n = int(input())
D = list(map(int, input().split()))
c = Counter(D)

total = 1
count = 0
for i in range(n):
  num = c.get(i, 0)
  if num == 0:
    total = 0
    break
  count += num
  if i == 0 and (c[i] != 1 or D[0] != 0):
    total = 0
  if i > 0:
    total = (total * (c[i - 1] ** c[i])) % 998244353
  if count == n:
    break
print(total)