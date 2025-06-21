n = input()
f = sum(list(map(int, list(n))))
x = int(n)
print('Yes' if x % f == 0 else 'No')