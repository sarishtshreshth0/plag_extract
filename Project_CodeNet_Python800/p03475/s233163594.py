N=int(input())
C,S,F=[],[],[]

for i in range(N-1):
    c,s,f=map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)

T=[0]*N
for i in range(N):
    A=0
    for j in range(i,N-1):
        if A>=S[j]:
            A=((A+F[j]-1)//F[j])*F[j]
        else:
            A=S[j]
        A+=C[j]
    T[i]=A

print("\n".join(map(str,T)))