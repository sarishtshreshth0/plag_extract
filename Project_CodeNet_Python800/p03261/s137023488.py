N=int(input())
W=[]
for i in range(N):
    W.append(input())
A=[]
for i in range(1,N):
    for j in range(0,i):
        if W[i]!=W[j] and W[i][0]==W[i-1][len(W[i-1])-1]:
            A.append('Yes')
        else:
            A.append('No')
if 'No' in A:
    print('No')
else:
    print('Yes')