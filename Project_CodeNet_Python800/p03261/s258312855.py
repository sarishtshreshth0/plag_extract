N = int(input())
f = 0
A = []
for i in range(N):
  if i == 0:
    A.append(input())
  else:
    A.append(input())
    if A[-2][-1] != A[-1][0]:
      f = 1
      break
    if len(set(A)) < i + 1:
      f = 1
      break
if f == 0:
  print("Yes")
else:
  print("No")