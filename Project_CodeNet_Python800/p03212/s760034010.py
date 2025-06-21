n=int(input())
d=["3","5","7"]
ans=[]
ans+=d
while d:
    a=d.pop(0)
    if len(a)<9:
        for i in "357":
            d+=[i+a]
            ans+=[i+a]
ans=list(map(int,ans))
ans.sort()
print(sum(i<=n for i in ans if len(set(str(i)))==3))