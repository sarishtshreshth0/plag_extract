import sys

def solve():
    input = sys.stdin.readline
    A, B, C, D = map(int, input().split())
    double  = 0
    for i in range(101):
        if A <= i <= B and C <= i <= D: double += 1
    print(double - 1 if double > 1 else 0)

    return  0

if __name__ == "__main__":
    solve()