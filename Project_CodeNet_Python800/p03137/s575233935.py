import itertools
n,m=map(int, input().split())
x=[int(i) for i in input().split()]
x.sort()
if(n>=m):
    print(0)
    exit()
dist = abs(x[-1]-x[0])

diff = []

for i in range(m-1):
    diff.append([abs(x[i]-x[i+1]),i])

diff.sort(key = lambda x:x[0],reverse = True)
for i in range(n-1):
    dist-=diff[i][0]
print(dist)
