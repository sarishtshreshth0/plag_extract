#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(N: int, K: int):
    ans = 0
    while N >= K:
        N //= K
        ans += 1

    
    print(ans+1)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)



if __name__ == "__main__":
    main()
