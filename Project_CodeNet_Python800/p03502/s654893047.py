n=input()
nx=int(n)
n=list(n)
n=[int(s) for s in n]
x=sum(n)

if nx%x==0:
    print('Yes')
else:
    print('No')