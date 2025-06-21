h,w=map(int,input().split())

if h==1 or w==1:
  print(1)
  exit()

ans=h*(w//2)

if w%2==1:
  ans+=(h+2-1)//2


print(ans)