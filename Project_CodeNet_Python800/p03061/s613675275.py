import sys
import fractions
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))


def solve():

    gcd_f = [0] * N
    gcd_b = [0] * N

    gcd_f[0] = A[0]
    for i in range(N - 1):
        gcd_f[i + 1] = fractions.gcd(gcd_f[i], A[i + 1])

    gcd_b[0] = A[-1]
    for i in range(N - 1):
        gcd_b[i + 1] = fractions.gcd(gcd_b[i], A[-i - 2])

    ans = gcd_f[-2]
    ans = max(ans, gcd_b[-2])

    # print(gcd_f)
    # print(gcd_b)

    for i in range(N - 2):
        t = fractions.gcd(gcd_f[i], gcd_b[-3 - i])
        #print(gcd_f[i], gcd_b[- 3 - i])
        ans = max(ans, t)

    print(ans)


if __name__ == '__main__':
    solve()
