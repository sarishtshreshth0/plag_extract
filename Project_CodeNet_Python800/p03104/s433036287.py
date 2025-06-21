def f(x):
  res=0
  cnt_xor=0
  cnt_xor=(x+2-1)//2
  if x%2==0:
    if cnt_xor%2==1:
      res=1^x
    else:
      res=0^x
  else:
    if cnt_xor%2==1:
      res=1
    else:
      res=0
  return res
a,b=map(int,input().split())
print(f(b)^f(a-1))
