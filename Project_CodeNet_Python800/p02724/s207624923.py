X = int(input())
n500 = int(X / 500)
n5 = int((X % 500) / 5)
print(n500 * 1000 + n5 * 5)
