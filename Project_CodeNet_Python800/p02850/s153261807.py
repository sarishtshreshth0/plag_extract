N=int(input())

A=[[] for _ in range(N-1)]
B=[0]*N
C=[0]*N
D=[0]*N

for i in range(N-1):
    a,b=map(int,input().split())
    A[a-1].append(b)
    C[b-1]=i+1

for i in range(N-1): 
    c=0
    for j in A[i]:
        while True:
            c+=1
            if c!=B[i]:
                B[j-1]=c
                break

print(max(B))            

for i in range(1,N):
    D[C[i]]=B[i]

for i in range(1,N):
    print(D[i])


