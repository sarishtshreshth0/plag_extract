

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))

def g(X):
    """
    000
    001
    010
    011
    100
    101
    110
    111
    """
    p = 1
    i = 39
    digits = [0]*40
    N = X+1
    while i > -1:
        digits[i] = N//(2*p)*p
        if N%(2*p)-p > 0:
            digits[i] += N%(2*p)-p
        p *= 2
        i -= 1
    answer = 0
    p = 1
    for d in digits[::-1]:
        if d%2 == 1:
            answer += p
        p *= 2
    return answer


def solve():
    """
    f(A, B) = A^...^B
    g(A) = 0^...^A
    g(B) = 0^...^B

    f(A, B) = g(A-1)^g(B)
    f(0, B) = g(B)
    """
    A, B = read_ints()
    if A == 0:
        return g(B)
    return g(A-1)^g(B)


if __name__ == '__main__':
    print(solve())
