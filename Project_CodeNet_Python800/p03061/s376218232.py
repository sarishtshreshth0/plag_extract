import sys,math,collections,itertools
input = sys.stdin.readline

N = int(input())
A=sorted(list(map(int,input().split())))
B = A[-1::-1]

GCA = [0]
GCB = [0]
for i in range(N):
    GCA.append(math.gcd(GCA[-1],A[i]))
    GCB.append(math.gcd(GCB[-1],B[i]))
GCB = GCB[-1::-1]

m=[]
for i in range(N):
    m.append(math.gcd(GCA[i],GCB[i+1]))
print(max(m))
