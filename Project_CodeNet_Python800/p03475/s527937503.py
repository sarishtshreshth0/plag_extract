import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
CSF = tuple(tuple(map(int, input().split())) for _ in range(N - 1))

ans = [0] * N
for i in range(N):
    time = 0
    for j in range(i, N - 1):
        c, s, f = CSF[j]
        d = max(0, time - s)
        ride = (d + f - 1) // f
        time = s + ride * f + c
    ans[i] = time

print(*ans, sep="\n")