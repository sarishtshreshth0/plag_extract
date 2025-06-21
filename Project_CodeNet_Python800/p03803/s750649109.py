a = list(map(int, input().split()))
a = [i if i != 1 else 14 for i in a]
if a[0] > a[1]:
    print('Alice')
elif a[0] == a[1]:
    print('Draw')
else:
    print('Bob')