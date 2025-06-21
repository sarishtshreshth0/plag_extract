N=int(input())
L=[]
x=1
L.append(input())
for i in range(N-1):
    W=input()
    if W in L:
        x=0
    L.append(W)
    if L[i][-1]!=L[i+1][0]:
        x=0
if x==1:
    print('Yes')
else:
    print('No')