Q,H,S,D=map(int,input().split())
N=int(input())
min1 = min(4*Q, 2*H, S)
min2 = min(8*Q, 4*H, 2*S, D)
if N%2==0:
    print(N//2*min2)
else:
    print(N//2*min2 + min1)
