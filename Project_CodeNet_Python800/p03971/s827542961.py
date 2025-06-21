def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, a, b = map(int, input().split())
    s = input()
    for ch in s:
        ans = 'Yes'
        if ch == 'c':
            ans = 'No'
        elif ch == 'a':
            if a > 0:
                a -=1
            elif b > 0:
                b -= 1
            else:
                ans = 'No'
        else:
            if b > 0:
                b -= 1
            else:
                ans = 'No'
        print(ans)


if __name__ == '__main__':
    main()