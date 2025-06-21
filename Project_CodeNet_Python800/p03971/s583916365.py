n,a,b=map(int,input().split())
for c in input():
  if c<"c":
    if c<"b" and a+b:
      if a:a-=1
      else:b-=1
      print("Yes")
    elif b:
      b-=1
      print("Yes")
    else:
      print("No")
  else:print("No")      