A, B = map(int, input().split())
if A == 1 or B == 1:
  print(1)
elif (A*B) % 2 == 0:
  print(A*B//2)
else:
  print(A*B//2+1)