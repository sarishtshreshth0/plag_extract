import math
N = int(input())
A = [list(map(int,input().split())) for _ in range(N-1)]
for i in range(N):
    t = 0
    for C,S,F in A[i:]:
        if t < S:
            t = S+C
        else:
            t = math.ceil((t-S)/F)*F+S+C
    print(t)