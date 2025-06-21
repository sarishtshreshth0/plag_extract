N = int(input())
A = list(map(int,input().split()))

X = [0]*N
Y = [0]*N

import fractions

X[0]=A[0]
for i in range(1,N):
    X[i] = fractions.gcd(X[i-1], A[i])

Y[N-1]=A[N-1]
for i in range(1,N):
    Y[N-1-i] = fractions.gcd(Y[N-i], A[N-1-i])

cand = []
cand.append(X[N-2])
cand.append(X[N-1])#=Y[0]
cand.append(Y[1])
for i in range(1,N-1):
    cand.append(fractions.gcd(X[i-1],Y[i+1]))

print(max(cand))
