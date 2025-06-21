Q,H,S,D = map(int,input().split())
N = int(input())
x2 = min(D,2*S,4*H,8*Q)
cnt = (N//2)*x2
N = N%2
x1 = min(S,2*H,4*Q)
cnt += N*x1
print(cnt)