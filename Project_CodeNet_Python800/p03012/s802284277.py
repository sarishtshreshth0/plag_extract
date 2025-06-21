n=int(input())
l=list(map(int,input().split()))
ans=[]
x=0
for i in range(n):
    x+=l[i]
    ans.append(abs(x-(sum(l)-x)))
print(min(ans))