N = int(input())

M = str(N)
d = 0
for i in range(len(M)):
  d += int(M[i])

if N%d == 0:
  print("Yes")
else:
  print("No")