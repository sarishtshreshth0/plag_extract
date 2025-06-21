N = int(input())
S = list(map(int, input().split()))
A = {}
t = 0
ans = 0
for s in S:
    t+=s
    if t == 0:
        ans+=1
    if t in A:
        A[t]+=1
        ans+=A[t]
    else:
        A[t]=0

print(ans)