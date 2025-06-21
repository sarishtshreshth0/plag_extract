def main():
    x, y = map(int, input().split())
    ans = solve(x, y)
    print(ans)


def solve(x, y):
    ans = x + y // 2
    return ans


if __name__ == '__main__':
    main()