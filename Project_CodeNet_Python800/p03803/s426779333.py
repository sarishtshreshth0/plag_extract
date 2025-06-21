a,b = map(int,input().split())
l=[0]*12
for i in range(2,14):
    l[i-2]=i
l.append(1)
if l.index(a)>l.index(b):
    print('Alice')
elif a==b:
    print('Draw')
else:
    print('Bob')