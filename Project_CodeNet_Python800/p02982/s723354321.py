N,D = map(int,input().split())
X = [list(map(int,input().split())) for _ in range(N)]
count = 0
for i in range(N):
    for j in range(i+1,N):
        s=0
        for k in range(D):
            s += (X[i][k]-X[j][k])**2
        s = s**0.5
        if(s==int(s)):
            count+=1
print(count)