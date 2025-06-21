LI = lambda: list(map(int, input().split()))

N = int(input())
W = LI()


def main():
    s = sum(W)
    ans = s
    x = 0
    for w in W:
        x += w
        ans = min(ans, abs(2 * x - s))
    print(ans)


if __name__ == "__main__":
    main()
