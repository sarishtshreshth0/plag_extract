n,k=map(int,input().split())
cnt=0
while(1):
  if n//(k**cnt) == 0:
    print(cnt)
    break
  cnt += 1