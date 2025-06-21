N = int(input())

fx = 0
Nx = N
for i in range(8):
  fx += Nx % 10
  Nx = Nx // 10
if N % fx == 0:
  print("Yes")
else:
  print("No")