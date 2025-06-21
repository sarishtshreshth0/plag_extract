n = input()
total = sum(list(map(int, list(n))))
num = int(n)
if num % total == 0:
    print('Yes')
else:
    print('No')
