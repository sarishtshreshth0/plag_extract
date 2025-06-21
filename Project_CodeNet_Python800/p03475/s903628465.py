#c
N=int(input())
CSF = [None]*(N-1)
for i in range(N-1):
    CSF[i] = list(map(int, input().split()) )

for I in range(N):
    now = 0
    for csf in CSF[I:]:
        now = max( -(-now//csf[2])*csf[2] , csf[1]) + csf[0]
    print(now)