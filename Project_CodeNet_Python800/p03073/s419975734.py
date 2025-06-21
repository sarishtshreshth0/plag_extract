S = list(input())
N = len(S)

B = ['0' for i in range(N)]
W = ['1' for i in range(N)]
for i in range(0,N,2):
    B[i] = '1'
    W[i] = '0'

X = 0
Y = 0
for i in range(N):
    if S[i] != B[i]:
        X += 1
    if S[i] != W[i]:
        Y += 1

print(min(X,Y))