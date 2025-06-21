h,w=map(int,input().split())
if h == 1 or w == 1:
  print(1)
else:
  div,mod=divmod(h*w,2)
  print(div+mod)