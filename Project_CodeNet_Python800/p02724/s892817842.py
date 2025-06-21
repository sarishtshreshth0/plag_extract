X = int(input())
n = X//500
ans = 1000*n
m = X%500
k = m//5
ans += 5*k
print(ans)