N,M = map(int,input().split())
X = list(map(int,input().split()))
if N >= M:
    print(0)
    exit()
X.sort()
A = []
for i in range(M-1):
    A.append(X[i+1]-X[i])
A.sort()
print(sum(A[:M-N]))