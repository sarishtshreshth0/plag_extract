A, B = map(int, input().split())
if A == 1:
  A = 15
if B == 1:
  B = 15
print("Alice" if A > B else "Draw" if A == B else "Bob")