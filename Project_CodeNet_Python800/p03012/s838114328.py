n=int(input())
w=list(map(int,input().split()))
s1,s2,ans=0,sum(w),1000
for t in range(n):
    s1+=w[t]
    s2-=w[t]
    if abs(s1-s2)<ans:
        ans=abs(s1-s2)
        
print(ans)