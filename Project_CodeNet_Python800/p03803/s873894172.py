import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B = MI()
if A == B:
    print('Draw')
    exit()
if A == 1:
    A = 14
if B == 1:
    B = 14
print('Alice' if A > B else 'Bob')
