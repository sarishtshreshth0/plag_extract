import sys

def solve():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    if A == 2 or B == 2: print("No")
    else: print("Yes")

    return 0

if __name__ == "__main__":
    solve()