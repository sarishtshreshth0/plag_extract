from _collections import defaultdict
n=int(input())
A=list(map(int,input().split()))

X=[A[0]]
for i in range(1,n):
    X.append(X[-1]+A[i])
Y=defaultdict(int)
for x in X:
    Y[x]+=1
ans=0
for y in Y.values():
    ans+=(y-1)*y//2
print(ans+Y[0])