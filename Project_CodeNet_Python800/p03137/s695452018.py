import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, m, *x = map(int, read().split())
    if n >= m:
        print(0)
        sys.exit()
    x.sort()
    sa = []
    pre = x[-1]
    for xe in x:
        sa.append(abs(xe - pre))
        pre = xe
    sa.sort()
    num = m - n
    r = sum(sa[:num])
    print(r)

if __name__ == '__main__':
    main()