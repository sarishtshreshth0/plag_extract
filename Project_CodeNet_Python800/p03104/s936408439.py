

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def f(B):
    '''
    000  = 1   = 0
    001
    010  = 1
    011
    100  = 1
    101
    '''
    B += 1
    if B%4 == 0:
        return 0
    if B%4 == 1:
        return B-1
    if B%4 == 2:
        return 1
    return (B-1)^1


def solve():
    A, B = read_ints()
    return f(A-1)^f(B)


if __name__ == '__main__':
    print(solve())
