X = int(input())
A = X // 500
B = X % 500

C = B // 5

ans = A * 1000 + C * 5
print(ans)