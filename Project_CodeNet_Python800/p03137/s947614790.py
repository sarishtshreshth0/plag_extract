n, m = map(int, input().split())
X = list(map(int, input().split()))

if m <= n:
    print(0)
    exit()

X.sort()
Y = []
for i in range(m-1):
    y = X[i+1]-X[i]
    Y.append(y)
Y.sort()
#print(Y)
ans = sum(Y[0:m-(n-1)-1])
print(ans)
