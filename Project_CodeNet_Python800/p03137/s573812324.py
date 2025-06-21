n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
y=[]
if n>=m:
    print(0)
    exit()
for i in range(m-1):
    y.append(x[i+1]-x[i])
z=sorted(y,reverse=True)
count=0
for i in range(n-1):
    count+=z[i]
print(x[-1]-x[0]-count)