import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]

N, A, B = ri_()
S = rs()
a = 0
b = 0
for i in S:
    if i == 'a':
        if a < A + B:
            print('Yes')
            a += 1
        else:
            print('No')
    elif i == 'b':
        if a < A + B and b <= B - 1:
            print('Yes')
            a += 1
        else:
            print('No')
        b += 1
    else:
        print('No')