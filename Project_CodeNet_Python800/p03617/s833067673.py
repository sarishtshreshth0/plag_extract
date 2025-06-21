Q,H,S,D = map(int,input().split())
N = int(input())


L2 = min(D,2*S,4*H,8*Q)
L1 = min(S,2*H,4*Q)

ans = 0

ans+= (N//2)*L2
ans+= (N%2) *L1
ans=int(ans)
print(ans)