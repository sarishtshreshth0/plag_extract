import math

n,d = map(int,input().split())
l = []

for i in range(n):
    array = list(map(int,input().split()))
    l.append(array)

def dist(a,b):
    cnt = 0
    for i in range(len(a)):
        cnt += (a[i]-b[i])**2
    return math.sqrt(cnt)

ans = 0
    
for i in range(n):
    for j in range(i+1,n):
        if dist(l[i],l[j])%1 == 0:
            ans+=1
print(ans)