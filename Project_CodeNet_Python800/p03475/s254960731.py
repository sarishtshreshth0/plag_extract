N = int(input())
A = [list(map(int,input().split())) for _ in range(N-1)]
A.insert(0,0)
B = [0 for _ in range(N+1)]
for i in range(1,N):
    C1,S1,F1 = A[i]
    T = S1
    for j in range(i+1,N):
        C2,S2,F2 = A[j]
        if T+C1>=S2:
            dt = (T+C1)%F2
            if dt>0:
                T += F2-dt+C1
            else:
                T += C1
        else:
            T = S2
        C1 = C2
        S1 = S2
        F1 = F2
    T += C1
    B[i] = T
for i in range(1,N+1):
    print(B[i])