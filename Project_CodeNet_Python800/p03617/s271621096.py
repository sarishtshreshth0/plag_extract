Q,H,S,D=map(int,input().split())
N=int(input())
if H > 2*Q:
    H=2*Q
if S > 2*H:
    S=2*H
if D < 2*S:
    ans = N//2*(D)+(N%2)*S
else:
    ans = N*S
print(ans)