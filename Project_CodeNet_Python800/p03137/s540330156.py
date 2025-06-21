import sys

N,M=map(int,input().split())
X=list(map(int,input().split()))

if N>=M:
    print(0)
    sys.exit()

X.sort()

Y=[0]*(M-1)
for i in range(M-1):
    Y[i]=X[i+1]-X[i]

Y=sorted(Y)[:-(N-M)]
print(sum(Y))