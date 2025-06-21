import sys
n,m = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
if n >= m:
    print(0)
    sys.exit()
for i in range(m-1):
    ls[i] = ls[i+1]-ls[i]
del ls[-1]
ls.sort()
if n == 1:
    print(sum(ls))
else:
    ls = ls[:-(n-1)]
    print(sum(ls))
