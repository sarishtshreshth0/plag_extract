from fractions import gcd  # use math.gcd with python 3.5~


def main():
    N = int(input())
    A = list(map(int, input().split(' ')))
    L, R = [0 for _ in range(N)], [0 for _ in range(N)]
    L[0], R[N - 1] = A[0], A[N - 1]
    for i in range(1, N):
        L[i] = gcd(L[i - 1], A[i])
    for j in range(N - 2, -1, -1):
        R[j] = gcd(R[j + 1], A[j])
    max_gcd = 0
    for i in range(N):
        if i == 0:
            g = R[1]
        elif i == N - 1:
            g = L[N - 2]
        else:
            g = gcd(L[i - 1], R[i + 1])
        max_gcd = max([g, max_gcd])
    print(max_gcd)


if __name__ == '__main__':
    main()