n,m = map(int,input().split())
x = sorted(list(map(int,input().split())))

import sys
if n>=m:
    print(0)
    sys.exit()

y = []
for i in range(m-1):
    y += [x[i+1]-x[i]]
y = sorted(y)
print(sum(y[:m-n]))