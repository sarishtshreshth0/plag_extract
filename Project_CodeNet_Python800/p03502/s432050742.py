N = int(input())
sum = 0
M = N
while M > 0:
  sum += M % 10
  M //= 10
if N % sum == 0:
  print("Yes")
else:
  print("No")