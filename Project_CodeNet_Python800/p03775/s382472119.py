n=int(input())
ans=float("INF")
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        j=n//i
        tmp=len(str(max(i,j)))
        ans=min(ans,tmp)
print(ans)