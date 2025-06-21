n=int(input())
a=sorted(list(map(int,input().split())))

r=0
l=0
ans=0
while r<n:
    if a[r]-a[l]<=2:
        if r-l+1>ans:
            ans=r-l+1
        r+=1
    else:
        l+=1
print(ans)