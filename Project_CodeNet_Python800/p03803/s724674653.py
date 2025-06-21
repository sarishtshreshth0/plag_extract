strength = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]

A, B = [strength.index(n) for n in map(int, input().split())]
if A > B:
    print('Alice')
elif A < B:
    print('Bob')
else:
    print('Draw')
