import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A, B, C, D = map(int, readline().split())
    start = max(A, C)
    end = min(B,D)
    print(max(end-start,0))

if __name__ == '__main__':
    main()
