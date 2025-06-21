h,w=map(int,input().split())
if h==1 or w==1:
  print(1)
  exit()
w-=1
even=int(w/2)+1
odd=int((w+1)/2)
if h%2==0:
  print( (even+odd)*h//2 )
else:
  print( (even+odd)*(h-1)//2 + even )