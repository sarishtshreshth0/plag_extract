import fractions

N,X = map(int, input().split())
S = list(map(int, input().split()))
S = [abs(s-X) for s in S]

gcd = S[0]
for k in range(N-1):
  gcd = fractions.gcd(gcd, S[k+1])
print(gcd)