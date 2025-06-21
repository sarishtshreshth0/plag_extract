N, M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
L = []

for i in range(M-1):
    L.append(X[i+1] - X[i])

L.sort()

if M - N <= 0:
    print(0)
else:
    print(sum(L[:M - N]))