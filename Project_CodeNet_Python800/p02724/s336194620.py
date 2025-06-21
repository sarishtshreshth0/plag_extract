N = int(input())
a = N // 500
N -= 500 * a
b = N // 5
print(a * 1000 + b * 5)
