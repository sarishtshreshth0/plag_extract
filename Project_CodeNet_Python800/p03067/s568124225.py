A, B, C = map(int, input().split())

if A < C < B:
  print("Yes")
elif B < C < A:
  print("Yes")
else:
  print("No")