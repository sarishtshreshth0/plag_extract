n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
ret = 0
for i in range(n-1):
    for j in range(i+1, n):
        meu = 0
        for y, z in zip(x[i], x[j]):
            meu += (y-z)**2
        if (meu**0.5).is_integer():
            ret += 1
print(ret)