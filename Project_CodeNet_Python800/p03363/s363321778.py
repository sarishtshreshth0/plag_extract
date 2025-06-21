def f(d,i):
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    return d
n=int(input())
a=list(map(int,input().split()))
l=[0]
for i in range(n):
    l.append(l[i]+a[i])
d=dict()
for i in l:
    d=f(d,i)
print(sum([i*(i-1)//2 for i in d.values()]))