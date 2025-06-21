import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    #A, B = 123, 456
    A, B = in_nn()
    d = defaultdict(lambda: 0)

    n = 1
    while n <= A:
        n *= 2
        r = A % n
        #print(n, r)
        if r >= n // 2:
            d[n] = (r - n // 2) % 2

    n = 1
    while n <= B:
        n *= 2
        r = B % n
        #print(n, r)
        if r >= n // 2:
            d[n] ^= (r - n // 2 + 1) % 2

    n = 2
    ans = 0
    while n <= max(A, B):
        n *= 2
        ans += (n // 2) * d[n]

    d = (B - A + 1) % 4
    if A % 2 == 0:
        if d == 2 or d == 3:
            ans += 1
    if A % 2 == 1:
        if d == 1 or d == 2:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
