def LI():
    return list(map(int, input().split()))


X = int(input())
ans = X//500*1000
X = X % 500
ans += X//5*5
print(ans)
