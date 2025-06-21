Q,H,S,D = map(int,input().split())
N = int(input())
Min = min(4*Q,2*H,S)
if Min > D/2:
    if N%2 == 0:
        print(N//2*D)
    else:
        print(N//2*D + Min)
else:
    print(Min*N)