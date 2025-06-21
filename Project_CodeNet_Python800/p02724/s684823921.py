X = int(input())

a1 = 1000
a2 = 5

n1 = X // 500
X -= n1 * 500
n2 = X // 5

print(n1 * a1 + n2 * a2)
