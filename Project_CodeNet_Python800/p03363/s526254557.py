N = int(input())
A = list(map(int, input().split()))
X = {}

S = [0]
for a in A:
    S.append(S[-1]+a)

for s in S:
    if s in X.keys():
        X[s] += 1
    else:
        X[s] = 1
    
ans = 0
for x in X:
    ans += (X[x]*(X[x]-1))//2

print(ans)