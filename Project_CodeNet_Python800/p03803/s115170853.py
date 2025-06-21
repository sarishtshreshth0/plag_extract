A,B = [int(i) for i in input().split()]
if A > B:
  if B != 1:
  	print("Alice")
  else:
    print("Bob")
elif A < B:
  if A != 1:
  	print("Bob")
  else:
    print("Alice")
else:
  print("Draw")