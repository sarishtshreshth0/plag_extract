A,B=map(int,input().split())
if A==B:
  print("Draw")
  exit()
if A==1:
  print("Alice")
  exit()
if B==1:
  print("Bob")
  exit()
if A>B:
  print("Alice")
  exit()
else:
  print("Bob")
  exit()