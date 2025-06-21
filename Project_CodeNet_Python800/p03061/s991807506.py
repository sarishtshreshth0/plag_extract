import sys
N=int(input())
A=list(map(int,input().split()))
A.sort()
MIN=A[1]
for i in range(MIN,0,-1):
  miss=0
  for k in range(N):
    if A[k]%i != 0:
      miss+=1
      if miss==2:
        break
    if k==N-1:
      ans=i
      print(ans)
      sys.exit()