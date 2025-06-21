X = int(input())

num1000 = X // 500
r500 = X % 500
num5 = r500 // 5

print(num1000 * 1000 + num5 * 5)
