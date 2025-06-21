# 約数列挙(nを含む)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)

            if i != n // i:
                divisors.append(n // i)

    return divisors


def solver(N, A):

    # 答えはA[0]かA[1]の約数
    p0 = make_divisors(A[0])
    p1 = make_divisors(A[1])
    P = list(set(p0 + p1))

    # 約数を大きい方から見る
    for p in sorted(P)[::-1]:
        c = 0
        for a in A:
            if a % p == 0:
                c += 1

        if c == N - 1 or c == N:
            return p


N = int(input())
A = list(map(int, input().split()))

ans = solver(N, A)
print(ans)

