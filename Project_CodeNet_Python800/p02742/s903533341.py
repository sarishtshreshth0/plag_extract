import sys
input = sys.stdin.readline


def read():
    H, W = map(int, input().strip().split())
    return H, W

def solve(H, W):
    if H == 1 or W == 1:
        return 1
    n = H * W
    return n // 2 + n % 2

if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
