import sys 
N, M = map(int, input().split())
X = list(map(int, input().split()))

X = sorted(X)

anslis = []


if M <= N:
    print(0)
    sys.exit()


    
for i in range(M-1):
    ans = abs(X[i+1] - X[i])
    anslis.append(ans)
    ans = 0

anslis = sorted(anslis)

if N==1:
    print(sum(anslis))
else:
    print(sum(anslis[0:M-N]))