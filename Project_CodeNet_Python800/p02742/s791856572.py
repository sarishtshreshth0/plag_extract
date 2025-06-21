(h,w) = list(map(int,input().split()))

if h==1 or w==1:
  print(1)
elif w%2==0:
  print(int((w//2)*h))
else:
  print((h-(h//2))*(int((w//2)+(w%2)))+(h//2)*(int((w//2))))