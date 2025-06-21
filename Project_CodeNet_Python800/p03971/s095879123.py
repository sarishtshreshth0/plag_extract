N,A,B = map(int,input().split())
S = input()

t1,t2 = 0,0
for ch in S:
  if ch == "c":
    print("No")
  elif ch == "a":
    if t1 >= A+B:
      print("No")
    else:
      t1 += 1
      print("Yes")
  else:
    if t1 >= A+B or t2 >= B:
      print("No")
    else:
      t1 += 1
      t2 += 1
      print("Yes")