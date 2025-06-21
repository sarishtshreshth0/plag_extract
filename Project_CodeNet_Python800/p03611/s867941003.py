N=int(input())
A=list(map(int,input().split()))

X={i:0 for i in range(-1,max(A)+2)}
for a in A:
    X[a]+=1
    X[a-1]+=1
    X[a+1]+=1

print(max(X.values()))
