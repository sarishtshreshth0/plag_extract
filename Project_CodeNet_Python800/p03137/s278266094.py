n, m = map(int, input().split())
X = list(map(int, input().split()))

if n >= m:
    print(0)
    exit()

X.sort()

if n == 1:
    print(X[-1]-X[0])
    exit()

Y = []
for i in range(m-1):
    Y.append(X[i+1]-X[i])
#print(Y)
Y.sort()
ans = sum(Y[0:-(n-1)])
print(ans)
