N, M = map(int,input().split())
X = list(map(int,input().split()))
if len(X)<2:
    print(0)
else:    
    X.sort()

    diffs = []
    for i in range(M-1):
        diffs.append(abs(X[i+1]-X[i]))
    diffs.sort(reverse=True)
    print(X[M-1]-X[0]-sum(diffs[:N-1]))