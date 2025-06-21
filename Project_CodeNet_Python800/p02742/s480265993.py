h,w=input().split(" ")
h,w=int(h),int(w)
if h==1 or w==1:
  print(1)
elif h*w%2==0:
  print(int(h*w/2))
else:
  print(int(h*w//2+1))