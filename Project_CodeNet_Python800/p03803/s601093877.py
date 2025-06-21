a,b=input().split()
a=int(a)
b=int(b)
if a==b:
  print("Draw")
else:
  if a==1:
    print("Alice")
  else:
    if b==1:
      print("Bob")
    else:
      if a-b>0:
        print("Alice")
      else:
        print("Bob")