a,b,c,d=map(int,input().split())
ans=0
for i in range(a,b+1):
    for j in range(c,d+1):
        if i==j:
            ans+=1
if ans>0:
    print(ans-1)
else:
    print(0)