N=int(input())
ans=len(str(N))
for a in range(2,int(N**0.5)+1):
    if N%a==0:
        b=N//a
        ans=min(ans,len(str(b)))
print(ans)