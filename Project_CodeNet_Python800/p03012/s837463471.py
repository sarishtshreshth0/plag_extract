n=int(input())
l=list(map(int,input().split()))
ans=100000
for i in range(n-1):
    ans=min(ans,abs(sum(l[:i+1])-sum(l[i+1:])))
print(ans)