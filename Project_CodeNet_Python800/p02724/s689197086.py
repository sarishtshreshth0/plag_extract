x = int(input())

p = x // 500
x = x - p * 500
q = x // 5
print(p * 1000 + q * 5)