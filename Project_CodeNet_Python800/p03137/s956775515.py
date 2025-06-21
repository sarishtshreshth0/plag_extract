import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
X = sorted(list(map(int,input().split())))
Xsub = []
for i in range(M-1):
    Xsub.append(X[i+1]-X[i])
    
Xsub = sorted(Xsub)

if N > 1:
    print(sum(Xsub[:-(N-1)] ))   
else:
    print(sum(Xsub))
