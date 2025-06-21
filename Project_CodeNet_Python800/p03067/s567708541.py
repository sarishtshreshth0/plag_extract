a,b,c=list(map(int, input().split()))
if c in range(min(a,b),max(a,b)+1):
  print("Yes")
else:
  print("No")