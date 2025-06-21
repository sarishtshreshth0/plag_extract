n,k=map(int,input().split())
ans=0
for i in range(100000000):
    if n>=1:
        n=n/k
        ans+=1
    else:
        print(ans)
        break