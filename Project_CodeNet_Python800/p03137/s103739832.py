N,M=map(int,input().split())
X=list(map(int,input().split()))
X.sort(key=int)
p=[0]*M
for i in range(1,M): p[i]=X[i]-X[i-1]
p.sort(key=int)
for i in range(min(N-1,M)): p.pop(-1)
print(sum(p))