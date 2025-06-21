import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
print(N if N % 2 == 0 else 2*N)
