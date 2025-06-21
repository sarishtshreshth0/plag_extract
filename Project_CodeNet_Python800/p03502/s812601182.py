import sys
input = sys.stdin.readline
N = int(input())
if N % sum(list(map(int, str(N)))) == 0: print("Yes")
else: print("No")