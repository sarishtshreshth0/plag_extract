def f(x):
    return sum(map(int, x))

x = input()
# print(f(x))
if int(x) % f(x):
    print('No')
else:
    print('Yes')
