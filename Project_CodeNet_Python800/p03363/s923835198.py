from collections import Counter
from operator import mul
from functools import reduce
def main():
    def combinations_count(n, r):
        r = min(r, n - r)
        numer = reduce(mul, range(n, n - r, -1), 1)
        denom = reduce(mul, range(1, r + 1), 1)
        return numer // denom
    n = int(input())
    A = list(map(int, input().split()))
    B = [0, ]
    s = 0
    for i in range(n):
        s += A[i]
        B.append(s)
    C = Counter(B).most_common()
    ans = 0
    for c in C:
        if c[1] >= 2:
            ans += combinations_count(c[1], 2)
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
