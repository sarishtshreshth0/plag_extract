import math
N = int(input())
A = [list(map(int,input().split())) for _ in range(N-1)]
A.insert(0,0)
for i in range(1,N):
    C,S,F = A[i]
    T = S+C
    j = i+1
    while j<N:
        C,S,F = A[j]
        T = max(S,math.ceil(T/F)*F)
        T += C
        j += 1
    print(T)
print(0)