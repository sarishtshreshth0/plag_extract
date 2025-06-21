a,b,c,d=map(int,input().split())

diff=min(b,d)-max(a,c)
if diff < 0:
  diff=0
print(diff)