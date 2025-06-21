N=int(input())
A=list(str(N))
for i in range(len(A)):
    A[i]=int(A[i])
if N%(sum(A))==0:
    print('Yes')
else:
    print('No')