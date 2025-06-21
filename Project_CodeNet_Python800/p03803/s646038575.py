A,B = map(int, input().split())
A = 15 if A == 1 else A
B = 15 if B == 1 else B

if A == B:
    print('Draw')
elif A < B:
    print('Bob')
elif A > B:
    print('Alice')