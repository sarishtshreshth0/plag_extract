def slove():
    import sys
    input = sys.stdin.readline
    a, b, c = list(map(int, input().rstrip('\n').split()))
    abc1 = sorted([a, b, c])
    if abc1[1] == c:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    slove()
