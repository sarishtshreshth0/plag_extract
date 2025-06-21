X = int(input())

yen_500 = X // 500
yen_5 = (X % 500) // 5

print(yen_500 * 1000 + yen_5 * 5)