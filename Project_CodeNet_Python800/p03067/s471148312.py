def slove():
    import sys
    input = sys.stdin.readline
    a, b, c = list(map(int, input().rstrip('\n').split()))
    if a < c < b or a > c > b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    slove()
