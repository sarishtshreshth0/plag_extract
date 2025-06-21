#!python3

LI = lambda: list(map(int, input().split()))

# input
N = int(input())
A = LI()


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    l, r = [None] * N, [None] * N
    l[0] = A[0]
    r[0] = A[-1]
    for i in range(1, N):
        l[i] = gcd(l[i - 1], A[i])
        r[i] = gcd(r[i - 1], A[-i - 1])
    
    ans = 1
    for i in range(N):
        if i == 0:
            x = r[-2]
        elif i == N - 1:
            x = l[-2]
        else:
            x = gcd(l[i - 1], r[N - i - 2])
        ans = max(ans, x)
    print(ans)


if __name__ == "__main__":
    main()
