n,m=map(int,input().split())
x=list(map(int,input().split()))
num=[]
if n>=m:
    ans=0
else:
    x.sort()
    for i in range(m-1):
        num.append(x[i+1]-x[i])
    num.sort()
    ans=sum(num[:m-n])
print(ans)
