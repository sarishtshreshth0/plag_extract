import sys
n,k = map(int, sys.stdin.readline().rstrip("\n").split())
ans = 0
while n != 0:
    n = n // k
    ans += 1
print(ans)