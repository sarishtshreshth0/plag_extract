n=int(input())
d=["3","5","7"]
ans=0
while d:
    a=d.pop(0)
    if int(a)<=n and len(set(a))==3:ans+=1
    if len(a)<9:
        for i in "357":d+=[i+a]
print(ans)