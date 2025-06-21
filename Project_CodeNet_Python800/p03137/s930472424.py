n,m=map(int,input().split())
a=sorted(map(int,input().split()))

p=[]
for x in range(m-1):
    p.append(a[x+1]-a[x])

if n==1:print(sum(p));exit()
print(sum(sorted(p)[:1-n]))