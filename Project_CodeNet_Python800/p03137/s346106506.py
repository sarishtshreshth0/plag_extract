N,M=map(int,input().split())
X=sorted(map(int,input().split()))
sa=[]
for i in range(1,M):
    sa.append(X[i]-X[i-1])
print(sum(sorted(sa,reverse=True)[N-1:]))