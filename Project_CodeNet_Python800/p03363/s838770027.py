import sys
from collections import Counter

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]

    c = Counter(S)
    ans = 0
    for v in c.values():
        ans += v*(v-1)//2
    print(ans)


if __name__ == "__main__":
    main()
