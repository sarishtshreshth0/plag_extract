import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B = map(int, readline().split())
    A -= 2
    B -= 2
    if A % 13 > B % 13:
        print('Alice')
    elif A % 13 < B % 13:
        print('Bob')
    else:
        print('Draw')


if __name__ == '__main__':
    main()
