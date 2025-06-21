A,B=map(int,input().split())
if((A!=1 and B!=1 and A>B)or(A==1 and B!=1)):
  print("Alice")
elif(A==B):
  print("Draw")
else:
  print("Bob")