def main():
    n = int(input())
    s = input()
    l, r = 0, 0
    for c in s:
        if c == '(':
            l += 1
        else:
            if l:
                l -= 1
            else:
                r += 1
    print('(' * r + s + ')' * l)


if __name__ == '__main__':
    main()