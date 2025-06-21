n,a,b=map(int,input().split())
for c in input():
  f=1
  if c<"b"and a+b>0:f=0;a-=1
  elif c<"c"and a+b>0and b>0:f=0;b-=1
  print("YNeos"[f::2])