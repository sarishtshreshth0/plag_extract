n=int(input())
l=[]
t=int(n**0.5)
while len(l)==0:
    if n%t==0:
        l.append((t,n//t))
    t-=1
x,y=l[0][0],l[0][1]
ans=max(len(list(str(x))),len(list(str(y))))
print(ans)