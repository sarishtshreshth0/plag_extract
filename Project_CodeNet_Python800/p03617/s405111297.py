Q, H, S, D = map(int,input().split())
N = int(input())
W = min(2*Q, H)
T = min(2*W, S)
E = min(2*T, D)
if N%2 == 0:
    ans = E * (N//2)
else:
    ans = E * (N//2) + T
print(ans)