n=int(input())
R=set([tuple(map(int,input().split())) for i in range(n)])
B=[tuple(map(int,input().split())) for i in range(n)]
B.sort()
ans=0
for a,b in B:
    x,y=-1,-1
    for c,d in R:
        if c<a and d<b and y<d:
            x,y=c,d
    if x>-1:
        ans+=1
        R.remove((x,y))
print(ans)