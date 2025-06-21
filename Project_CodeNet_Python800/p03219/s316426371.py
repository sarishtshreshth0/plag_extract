x ,y = map(int, input().split())
if 1 <= x <= 100 and 2 <= y <= 100 and 0 == y % 2:
    print(int(x + y / 2))
else:
    print('hoge!')