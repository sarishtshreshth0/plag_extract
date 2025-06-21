A, B = map(int, input().split())
C = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
if C.index(A) > C.index(B):
    print('Alice')
elif C.index(A) < C.index(B):
    print('Bob')
else:
    print('Draw')