N=int(input())
W=list(map(int,input().split()))
l=[]
for i in range(1,N+1):
    S1=0
    S2=0
    for j in range(N):
        if (j+1)<=i:
            S1+=W[j]
        else:
            S2+=W[j]
    l.append(abs(S1-S2))
print(min(l))