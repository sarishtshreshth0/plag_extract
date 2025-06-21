H,W=map(int,input().split())
if H==1 or W==1:
  print(1)
elif H%2==0 or W%2==0:
  print(int(W/2*H))
else:
  ans=W*(H-1)/2+(W+1)/2
  print(int(ans))