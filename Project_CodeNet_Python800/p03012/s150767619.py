N = int(input())
W = list(map(int,input().split()))

val = 1000
for i in range(N-1):
  S1 = sum(W[:i+1])
  S2 = sum(W[i+1:N])
  val = min(val, abs(S1-S2))
print(val)