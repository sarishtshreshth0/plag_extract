import math
def main():
  n,d = list(map(int,input().split()))
  x = [input().split() for l in range(n)]
  ans=0
  for i in range(0,n):
    for j in range(i+1,n):
      dist=0
      for k in range(0,d):
        dist+=abs(int(x[j][k])-int(x[i][k]))*abs(int(x[j][k])-int(x[i][k]))
      if math.sqrt(dist)%1==0:
        ans+=1
  print(ans)
main()