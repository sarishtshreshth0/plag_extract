A, B = map(int, input().split())
C = []
for i in range(2,14):
  C.append(i)
C.append(1)

if C.index(A) < C.index(B):
  print("Bob")
elif C.index(A) == C.index(B):
  print("Draw")
else:
  print("Alice")