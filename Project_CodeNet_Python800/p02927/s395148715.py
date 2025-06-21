m,d=map(int,input().split())
l=list(range(1,m+1))
ans=0
for i in range(1,d+1):
    d_1=i%10
    d_10=(i-d_1)//10
    if d_1*d_10  in l and d_1!=1 and d_10!=1:
        ans+=1
print(ans)