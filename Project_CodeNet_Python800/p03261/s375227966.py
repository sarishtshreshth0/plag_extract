N=int(input())
W=[input()]*N
for i in range(1,N):
    W[i]=input()
    if W[i-1][-1]!=W[i][0]:print('No');exit()
if len(set(W))==N:print('Yes')
else:print('No')