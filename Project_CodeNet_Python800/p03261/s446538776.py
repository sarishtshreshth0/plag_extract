N=int(input())
A=[]
for _ in range(N):
    W=input()
    if W in A:
        print('No')
        exit()
    else:
        A.append(W)

for i in range(N-1):
    if A[i][-1]!=A[i+1][0]:
        print('No')
        exit()
print('Yes')