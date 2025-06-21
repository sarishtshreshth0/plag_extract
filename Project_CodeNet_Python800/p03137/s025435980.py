N,M=map(int,input().split())
*X,=map(int,input().split())
X.sort()

count=[0]*(M-1)
i=1
while i<M:
    count[i-1]=X[i]-X[i-1]
    i+=1
count.sort()

print(sum(count[:max(M-N,0)]))