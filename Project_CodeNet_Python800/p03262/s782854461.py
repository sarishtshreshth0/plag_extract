def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
  
N,X = map(int,input().split())
A = list(map(int,input().split()))
B = [abs(X-i) for i in A]
ans = B[0]
for j in B:
    ans = gcd(ans, j)
print(ans)