X = int(input())

A = 0
B = 0

if X >= 500:
    A = X // 500
    X = X % 500
if X >= 5:
    B = X // 5
    X = X % 5

print(A * 1000 + B * 5)