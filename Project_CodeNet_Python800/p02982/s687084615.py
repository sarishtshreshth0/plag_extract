import  math

n, d = map(int, input().split())
x = []
ans = 0

for i in range(n):
    X = list(map(int,input().split()))
    x.append(X)

for i in range(n):
    val = x[i]
    for j in range(i+1, n):
        val1 = x[j]
        val2 = 0
        for r in range(d):
            val2 += (val[r] - val1[r])**2
        if math.sqrt(val2).is_integer():
            ans += 1

print(ans)