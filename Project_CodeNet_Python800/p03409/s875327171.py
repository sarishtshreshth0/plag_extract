    #できなかった
n=int(input())
r=sorted([list(map(int,input().split())) for i in range(n)])
b=sorted([list(map(int,input().split())) for i in range(n)])
ans=0
for bx,by in b:
    ypoint=-1
    index=-1
    for num,(rx,ry) in enumerate(r):
        if bx>rx and by>ry and ypoint < ry:
            ypoint=ry
            index =num
    if ypoint>=0:
        ans+=1
        r.pop(index)
print(ans)
