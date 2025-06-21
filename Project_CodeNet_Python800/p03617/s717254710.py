A = list(map(int, input().split()))
N = int(input())

a = min(A[0]*4, A[1]*2, A[2])
b = A[3]

ans = min(N * a, N//2*b + (N%2)*a)
print(ans)
