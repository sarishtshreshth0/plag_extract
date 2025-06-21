import math


def main():
    n, s = map(int, input().split())
    xs = sorted(list(map(int, input().split())))

    for i in range(n):
        xs[i] = abs(xs[i] - s)

    for i in range(1, n):
        xs[i] = math.gcd(xs[i], xs[i-1])

    print(xs[n-1])


if __name__ == "__main__":
    main()
