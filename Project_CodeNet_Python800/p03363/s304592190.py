n=int(input())

A=list(map(int,input().split()))

U=[0]
for i in range(n):
    U.append(U[i]+A[i])

U.sort()

lis=[]
nlis=[]
for ui in U:
    if lis==[] or lis[-1]!=ui:
        lis.append(ui)
        nlis.append(1)
    else:
        nlis[-1]+=1

c=0
for n in nlis:
    c+=(n*(n-1))//2

print(c)