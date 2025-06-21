a,b=map(int,input().split())
if a==b:
  print(a)
  exit(0)
ans=0
if a&1:
  ans=a
  a+=1
if ((b-a+1)//2)&1:ans^=1
if not(b&1):ans^=b
print(ans)