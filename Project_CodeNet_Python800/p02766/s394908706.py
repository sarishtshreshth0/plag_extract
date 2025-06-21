n, k = [int(i) for i in input().split()]
cnt = 0
if n == 0:
  print(1)
  exit()
while n != 0:
  n = n // k
  cnt += 1
print(cnt)