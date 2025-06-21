import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    W = [int(w) for w in input().split()]
    wt = [0] * (N + 1)
    for i, w in enumerate(W):
        wt[i+1] = wt[i] + w
    minD = 1000000
    for i in range(N):
        minD = min(minD, abs(wt[i+1] - (wt[N] - wt[i+1])))
    print(minD)

    return 0

if __name__ == "__main__":
    solve()