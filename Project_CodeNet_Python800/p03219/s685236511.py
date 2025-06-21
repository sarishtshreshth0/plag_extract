def slove():
    import sys
    input = sys.stdin.readline
    x, y = list(map(int, input().rstrip('\n').split()))
    print(x + y // 2)


if __name__ == '__main__':
    slove()
