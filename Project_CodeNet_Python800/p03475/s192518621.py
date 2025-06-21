N=int(input())
C,S,F=[0]*(N-1),[0]*(N-1),[0]*(N-1)
for i in range(N-1):
    C[i],S[i],F[i]=map(int,input().split())

for i in range(N-1):
    time=0
    for j in range(i,N-1):
        if time%F[j]==0:
            if time>=S[j]:
                time+=C[j]
            else:
                time=S[j]
                time+=C[j]
        else:
            if time>=S[j]:
                time+=F[j]-time%F[j]
                time+=C[j]
            else:
                time=S[j]
                time+=C[j]
    print(time)
print(0)