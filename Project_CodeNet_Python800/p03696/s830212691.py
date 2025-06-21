def main():
    n = int(input())
    s = input()

    l, r = 0, 0

    for i in s:
        if i == ")":
            if l:
                l -= 1
            else:
                r += 1
        else:
            l += 1

    print(r * "(" + s + ")" * l)


if __name__ == '__main__':
    main()
