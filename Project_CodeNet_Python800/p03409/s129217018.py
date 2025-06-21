import bisect
n=int(input())
X=[]
for i in range(n):
    a,b=map(int,input().split())
    X.append([a,b,0])
for i in range(n):
    c,d=map(int,input().split())
    X.append([c,d,1])

X.sort(key=lambda x:x[0])

R=[]
ans=0
for i in range(2*n):
    if X[i][2]==0:
        R.append(X[i][1])
        R.sort()
    if X[i][2]==1:
        if len(R)==0:
            continue
        if min(R)>X[i][1]:
            continue
        R.pop(bisect.bisect_left(R,X[i][1])-1)
        ans+=1
print(ans)