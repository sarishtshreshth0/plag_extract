N = int(input())
a = list(map(int,input().split()))

ans = 0
numcnt = [0]*100001

for i in a:
    numcnt[i]+=1
    
for x in range(1,100000):
    subans = numcnt[x-1]+numcnt[x]+numcnt[x+1]
        
    ans = max(ans,subans)
    
print(ans)