import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():

    N = in_n()
    S = in_s()

    ts = S
    while ts.count('()'):
        ts = ts.replace('()', '')

    S = '(' * ts.count(')') + S + ')' * ts.count('(')
    print(S)


if __name__ == '__main__':
    main()
