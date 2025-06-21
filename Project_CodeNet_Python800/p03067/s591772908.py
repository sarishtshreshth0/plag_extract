a,b,c = map(int,input().split())
if a - c < 0:
  flag = "A"
else:
  flag = "B"
  
if (a <= c <= b and flag == "A") or (a >= c >= b and flag == "B") :
  print("Yes")
else:
  print("No")


