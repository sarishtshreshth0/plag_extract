import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    q, h, s, d = map(int, input().split())
    N = int(input())

    one = min([4*q, 2*h, s])
    print(min((N//2)*d+one*(N % 2), N*one))


resolve()