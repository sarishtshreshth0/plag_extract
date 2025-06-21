Q,H,S,D = map(int,input().split())
N = int(input())
H=min(2*Q,H)
S=min(2*H,S)
if 2*S < D:
    print(N*S)
else:
    if N%2==0:
        print((N//2)*D)
    else :
        print((N//2)*D+S)
