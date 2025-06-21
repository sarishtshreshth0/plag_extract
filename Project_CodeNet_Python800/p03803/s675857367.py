# 入力
a, b = map(int, input().split())

# 処理&出力
if a == b:
    print('Draw')
elif a == 1:
    print('Alice')
elif b == 1:
    print('Bob')
elif a > b:
    print('Alice')
elif b > a:
    print('Bob')