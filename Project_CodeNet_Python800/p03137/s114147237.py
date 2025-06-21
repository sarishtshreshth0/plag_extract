n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
a=[]
for i in range(m-1):
    a.append(abs(x[i+1]-x[i]))
a.sort()
al=sum(a)
if n==1:
    print(al)
else:
    a_skip=sum(a[-n+1:])
    print(al-a_skip)