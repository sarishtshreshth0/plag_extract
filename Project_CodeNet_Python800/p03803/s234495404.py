A, B = map(int, input().split())
A = (A - 2) % 13
B = (B - 2) % 13
if A < B:
  print("Bob")
elif A == B:
  print("Draw")
else:
  print("Alice")