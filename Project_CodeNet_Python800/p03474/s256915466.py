a,b=map(int,input().split())
N=list(str(input()))
if N[a]=="-":
  N.pop(a)
  if "-" in N:
    print("No")
  else:
    print("Yes")
else:
  print("No")