X = int(input())
ans = 0
ans += 1000 * (X // 500)
X = X % 500
ans += 5 * (X // 5)
print(ans)
