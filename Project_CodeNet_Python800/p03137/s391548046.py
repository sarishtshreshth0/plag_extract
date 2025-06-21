N,M = list(map(int,input().split())) 
X = sorted(list(map(int,input().split())))
A= []
for i in range(M-1):
    A.append(X[i+1] - X[i])
A = sorted(A,reverse = True)

print(sum(A[N-1:]))