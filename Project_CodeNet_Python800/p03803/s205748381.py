A,B=[int(i) for i in input().split(" ")]
if A==B:
  print("Draw")
elif (A==1) or (A>2 and (A>B) and B!=1) :
  print("Alice")
else: 
  print("Bob")
