X = int(input())
n = X//500
m = X % 500//5
ans = n*1000 + m*5
print(ans)
