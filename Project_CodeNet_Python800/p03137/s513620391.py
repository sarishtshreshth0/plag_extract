N,M = list(map(int,input().split()))
X = sorted(list(map(int,input().split())))
A = []
if N >= M:
    print(0)
    exit()
for i in range(M-1):
    A.append(X[i+1]-X[i])
print(X[-1]-X[0]-sum(sorted(A,key=lambda x: -x)[:N-1]))