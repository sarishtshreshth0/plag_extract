N = int(input())
W = [input() for i in range(N)]

ok = True
for i in W:
    if W.count(i)>1:
        ok = False
        
for i in range(1,N):
    if W[i-1][-1] != W[i][0]:
        ok = False
        
if ok:
    print('Yes')
else:
    print('No')