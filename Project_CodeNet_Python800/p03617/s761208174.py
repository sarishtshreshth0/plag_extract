*A,N  = map(int,open(0).read().split())
ans = 0
ans += (N//2)*min(A[0]*8,A[1]*4,A[2]*2,A[3])# 2x
ans += (N%2)*min(A[0]*4,A[1]*2,A[2])# 1x

print(ans)