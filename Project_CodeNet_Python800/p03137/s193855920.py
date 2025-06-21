n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=[]
for i in range(m-1):
    b.append(a[i+1]-a[i])
b_sort=sorted(b,reverse=1)
print(sum(b_sort[n-1:]))    