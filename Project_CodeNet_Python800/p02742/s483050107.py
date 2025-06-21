x,y=list(map(int,raw_input().split()))
w=x
h=y
if x==1 or y==1:
  print("1")
  exit(0)
ans=x//2 * (h//2 + (h+1)//2)
if x%2==1:
     ans+=(h+1)//2
print(ans) 