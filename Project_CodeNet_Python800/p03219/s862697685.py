def solve(inp):
    (X, Y) = map(int, inp.readline().strip().split(' '))

    return str(int(X + Y / 2))


def test(s):
    from io import StringIO
    print(solve(StringIO(s)))


def main():
    import sys
    result = solve(sys.stdin)
    if result:
        print(result)


if __name__ == '__main__':
    # test('')
    main()
