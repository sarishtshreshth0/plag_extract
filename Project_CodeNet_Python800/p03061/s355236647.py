def gcd(a,b):
    if a == 0 or b == 0:
        return max(a,b)
    return a if b==0 else gcd(b,a%b)
N = int(input())
A = list(map(int,input().split()))
rA = A[::-1]

LEFT = [0]
g = A[0]
for i in range(N):
    g = gcd(g,A[i])
    LEFT.append(g)


RIGHT = [0]
g = rA[0]
for i in range(N):
    g = gcd(g,rA[i])
    RIGHT.append(g)


ans = 0
for i in range(1,N+1):
    ans = max(ans,gcd(LEFT[i-1],RIGHT[N-i]))
print(ans)