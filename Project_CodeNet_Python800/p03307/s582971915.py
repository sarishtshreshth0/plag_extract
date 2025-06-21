import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    print(N if N % 2 == 0 else 2 * N)

    return  0

if __name__ == "__main__":
    solve()