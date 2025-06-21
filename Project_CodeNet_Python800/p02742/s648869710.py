h,w=input().split(' ')
h=int(h)
w=int(w)
if h==1 or w==1:
  print(1)
else:
  print(((h*w)+1)//2)