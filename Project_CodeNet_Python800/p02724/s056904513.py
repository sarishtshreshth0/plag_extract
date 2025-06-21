X = int(input())
a = X // 500
X -= a * 500
b = X // 5
print(a * 1000 + b * 5)