from math import gcd


def main():
    n, x = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.append(x)
    xs.sort()
    diff = []
    for i in range(1, n+1):
        diff.append(xs[i] - xs[i-1])
    ans = diff[0]
    for i in range(1, n):
        ans = gcd(ans, diff[i])
    print(ans)


if __name__ == "__main__":
    main()
