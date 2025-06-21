import sys
import math

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    CSF = list(list(map(int, readline().split())) for _ in range(N-1))
    T = []
    for i in range(N-1):
        t = 0
        for c, s, f in CSF[i:]:
            t = max(math.ceil(t/f)*f, s) + c
        T.append(t)
    T.append(0)
    for t in T:
        print(t)


if __name__ == '__main__':
    main()
