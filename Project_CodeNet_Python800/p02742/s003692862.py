h,w = map(int,input().split())
a = h*w
if h ==1 or w ==1:
  print(1)
elif a%2 == 1:
  print(round(a//2+1))
else:
  print(round(a/2))