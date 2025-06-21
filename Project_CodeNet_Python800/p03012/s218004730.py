N = int(input())
W = list(map(int, input().split()))
S = sum(W)
m = S
for i in range(1, N):
  T = sum(W[:i])
  m = min(m, abs(T-(S-T)))
print(m)