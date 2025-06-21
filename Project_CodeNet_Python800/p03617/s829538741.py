Q,H,S,D = map(int,input().split())
N = int(input())
cnt = (N//2)*min(8*Q,4*H,2*S,D)
if N%2==1:
    cnt += min(4*Q,2*H,S)
print(cnt)