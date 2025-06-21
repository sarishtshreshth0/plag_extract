def nx(t,s,f):
    if t<s:
        return s
    elif (t-s)%f==0:
        return t
    else:
        return t+f-t%f
n = int(input())
C,S,F = [0]*n, [0]*n, [0]*n
for i in range(n-1):
    C[i], S[i], F[i] = map(int, input().split())

for i in range(n):
    ans = 0
    for j in range(i, n-1):
        ans = nx(ans,S[j],F[j])+C[j]
    print(ans)