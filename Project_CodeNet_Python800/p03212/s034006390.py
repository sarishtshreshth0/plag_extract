def dfs(s, n):
    if int(s) > n:
        return 0
    if all(s.count(c) > 0 for c in '753'):
        result = 1
    else:
        result = 0
    for c in '753':
        result += dfs(s + c, n)

    return result


def main():
    n = int(input())
    print(dfs('0', n))


if __name__ == '__main__':
    main()
