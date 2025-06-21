import sys
N = int(input())
if not (1 <= N <= 10 ** 9):
    sys.exit()

print(N) if N % 2 == 0 else print(N * 2) 