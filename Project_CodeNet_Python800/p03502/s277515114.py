N = int(input())
M = N
X = 0
while M:
  X += M % 10
  M //= 10
if N % X == 0:
  print("Yes")
else:
  print("No")