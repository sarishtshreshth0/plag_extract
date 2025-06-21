mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    q, h, s, d = map(int, input().split())
    N = int(input())

    h = min(h, q*2)
    s = min(s, h*2)
    d = min(d, s*2)
    print(d * (N//2) + s * (N%2))


if __name__ == '__main__':
    main()
