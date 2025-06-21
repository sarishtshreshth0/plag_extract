n = int(input())
if 1 <= n <= 10 ** 9:
    if 0 == n % 2:
        print(n)
    else:
        print(n * 2)
else:
    print('hoge!')