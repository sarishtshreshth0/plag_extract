

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    A, B = read_ints()
    if A == B:
        return 'Draw'
    if (A == 1 and B == 13):
        return 'Alice'
    if (A == 13 and B == 1):
        return 'Bob'
    if A > B:
        return 'Alice'
    return 'Bob'


if __name__ == '__main__':
    print(solve())
