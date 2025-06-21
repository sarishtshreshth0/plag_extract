n=int(input())
flag=True
a=0
l=[]
for i in range(n):
    b=a
    l.append(b)
    a=list(input())
    if i>0:
        if a[0]!=b[-1] or a in l:
            flag=False
if flag:
    print('Yes')
else:
    print('No')