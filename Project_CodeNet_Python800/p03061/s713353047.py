import fractions
N = int(input())
A = list(map(int, input().split()))
right = [A[0]]*N
left = [A[-1]]*N
for i in range(1,N):
    right[i] = fractions.gcd(right[i-1],A[i])
    left[N-1-i] = fractions.gcd(left[N-i],A[N-1-i])
ans = left[1]
for i in range(N-2):
    ans = max(ans,fractions.gcd(right[i],left[i+2]))
print(max(ans,right[N-2]))
