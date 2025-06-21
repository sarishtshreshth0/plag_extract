import sys

N,K=map(int,input().split())

if N<K:
    print(1)
    sys.exit()

M=K
R=1
while M<=N:
    M*=K
    R+=1
print(R)