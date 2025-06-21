n,k=map(int,input().split())
for i in range(37):
    if n<(k**i):
        ans=i
        break
print(ans)