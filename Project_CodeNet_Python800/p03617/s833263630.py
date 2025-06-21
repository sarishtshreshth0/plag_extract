Q,H,S,D=map(int,input().split())
N=int(input())
a=0
if N%2:
    a+=min(4*Q,2*H,S)
a+=N//2*min(8*Q,4*H,2*S,D)
print(a)