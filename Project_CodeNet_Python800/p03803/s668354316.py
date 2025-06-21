import sys

A, B = list(map(int, input().split()))

if A == B:
  print("Draw")
  sys.exit()

if A == 1:
  A = 14
elif B == 1:
  B = 14

if A > B:
  print("Alice")
else:
  print("Bob")