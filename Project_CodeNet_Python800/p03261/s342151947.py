N = int(input())
S=[]

for n in range(N):
    s=input()
    S.append(s)
S_set=set(S)

ans='Yes'
if len(S_set) != N:
    ans='No'

for n in range(N-1):
    n_ = n+1
    s_0=S[n][-1]
    s_1=S[n_][0]
    
    if s_0 != s_1:
        ans='No'
print(ans)