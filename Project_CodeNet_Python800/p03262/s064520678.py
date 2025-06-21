from fractions import gcd

def mi():
    return map(int, input().split())

def main():
    N, X = mi()
    x = list(mi())
    y = [abs(x[i]-X) for i in range(N)]
    t = y[0]
    for i in range(N):
        t = gcd(t, y[i])
    print(t)


if __name__ == '__main__':
    main()