def main():
    N = int(input())

    memo = set()
    prev = ''
    for _ in range(N):
        s = input()
        if prev and ((prev[-1] != s[0]) or (s in memo)):
            print('No')
            return
        memo.add(s)
        prev = s

    print('Yes')


if __name__ == '__main__':
    main()
