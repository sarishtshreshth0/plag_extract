import sys
input = sys.stdin.readline
import math
from fractions import gcd
import operator
from functools import reduce
from itertools import accumulate

def read():
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    return N, A


def prime_factorization_preprocess(n):
    """
    エラトステネスの篩を用いて、sqrt(n)以下の素数を列挙する
    """
    m = math.floor(math.sqrt(n)) + 1
    primes = []
    is_prime = [True for i in range(m)]
    for i in range(2, m):
        if is_prime[i]:
            primes.append(i)
            for j in range(i+i, m, i):
                is_prime[j] = False
    return primes


def prime_factorization(x, primes):
    """
    試し割り法により、数値の素因数分解を求める
    """
    factors = defaultdict(int)
    for p in primes:
        if x % p == 0:
            n = 0
            while x % p == 0:
                x //= p
                n += 1
            factors[p] = n
    return factors


def solve(N, A, AMAX = 10**9, INF=10**9):
    sl = list(accumulate(A, gcd))
    sr = list(reversed(list(accumulate(reversed(A), gcd))))
    max_gcd = sl[-1]
    for i in range(N):
        # gcdの単位元は0
        v = 0
        if i > 0:
            v = gcd(v, sl[i-1])
        if i < N-1:
            v = gcd(v, sr[i+1])
        max_gcd = max(max_gcd, v)
    return max_gcd


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
