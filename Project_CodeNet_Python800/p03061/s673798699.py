import sys
from fractions import gcd
def input(): return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    """
    「中間の値に関してうんぬん　→　その値の左右の区間から計算」
    は定石と思っていい気がする。

    言われてみればA[i]を除いたGCDはgcd(A[:i])とgcd(A[i+1:])から求まるわなあ
    素因数分解してとか考える以前の話だった。。。
    """

    L = [0] * (N + 1)    # L[i] = gcd(A[:i])
    R = [0] * (N + 1)    # R[i] = gcd(A[i:])
    L[1] = A[0]
    R[N - 1] = A[N - 1]
    for i in range(2, N + 1):
        L[i] = gcd(L[i - 1], A[i - 1])
    for i in range(N - 2, -1, -1):
        R[i] = gcd(R[i + 1], A[i])

    ans = R[1]
    for i in range(1, N - 1):
        ans = max(ans, gcd(L[i], R[i + 1]))
    ans = max(ans, L[N - 1])
    print(ans)


if __name__ == "__main__":
    main()
