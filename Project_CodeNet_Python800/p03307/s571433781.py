def slove():
    import sys
    import fractions
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    print(2 * n // fractions.gcd(n, 2))


if __name__ == '__main__':
    slove()
