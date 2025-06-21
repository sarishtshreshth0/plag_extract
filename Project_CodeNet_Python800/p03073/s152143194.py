S=input()
N=len(S)

tile1=('10'*N)[:N]
tile0=('01'*N)[:N]

ans1=0
ans0=0
for i in range(N):
    ans1+=S[i]!=tile1[i]
    ans0+=S[i]!=tile0[i]

print(min(ans1,ans0))