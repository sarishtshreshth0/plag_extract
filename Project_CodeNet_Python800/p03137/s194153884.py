import sys
N,M = map(int,input().split())
if N >= M:
    print(0)
    sys.exit()
    
lc = list(map(int,input().split()))
lc.sort()
#print(lc)

diff = []
for i in range(M-1):
    diff.append(lc[i+1]-lc[i])
    
#print(diff)
diff.sort()
diff_min = diff[:M-N]
print(sum(diff_min))