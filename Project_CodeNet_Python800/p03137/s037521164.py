def main():
    # n = int(input())
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in range(n)]

    x.sort()

    subs = []

    for i in range(1, m):
        subs.append(abs(x[i]-x[i-1]))

    subs.sort()
    if (m < n):
        print(0)
    else:
        print(sum(subs[0:m-n]))


if __name__ == '__main__':
    main()
