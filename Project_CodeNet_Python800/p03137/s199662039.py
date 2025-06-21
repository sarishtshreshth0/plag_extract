n,m=list(map(int,input().split()))
x=list(map(int,input().split()))
import sys
if n>m:
  print(0)
  sys.exit()

x.sort()
ans_list=[]
for i in range(1,m):
  ans_list.append(x[i]-x[i-1])
ans_list.sort(reverse=True)

print(max(x)-min(x)-sum(ans_list[:n-1]))


