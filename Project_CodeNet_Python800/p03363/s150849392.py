from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
 
sm=[0]*(n+1)
d=defaultdict(int)
for i in range(1,n+1):
    sm[i]=sm[i-1]+a[i-1]
    d[sm[i]]+=1
 
d[0]+=1
ans=0
for i,j in d.items():
    ans+=(j*(j-1))//2
 
print(ans)