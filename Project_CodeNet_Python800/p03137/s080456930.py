N,M=map(int,input().split())
S=list(map(int,input().split()))
S.sort()
L=[0]*(M-1)
for i in range(M-1):
    L[i]=abs(S[i]-S[i+1])

L.sort()
goukei=0
if M-N>=1:
    for i in range(M-N):
        goukei+=L[i]
else:
    print(0)
    exit()
print(goukei)