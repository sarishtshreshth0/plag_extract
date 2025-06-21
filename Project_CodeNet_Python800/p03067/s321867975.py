import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, C = map(int, readline().split())
    if A<C<B or A>C>B:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()