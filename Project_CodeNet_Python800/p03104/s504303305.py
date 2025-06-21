from math import ceil
def f(x):
  xor_cnt=ceil(x/2)
  res=0
  if x%2==1:
    if xor_cnt%2==0:
      res=0
    else:
      res=1
  else:
    if xor_cnt%2==0:
      res=0^x
    else:
      res=1^x
  return res

a,b=map(int,input().split())
print(f(b)^f(a-1))
