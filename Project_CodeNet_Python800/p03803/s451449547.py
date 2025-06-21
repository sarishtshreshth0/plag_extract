a,b=map(int,input().split())
if a==1:
  if b==1:
    print("Draw")
  else:
    print("Alice")
else:
  if b==1:
    print("Bob")
  else:
    if a==b:
      print("Draw")
    elif a<b:
      print("Bob")
    else:
      print("Alice")