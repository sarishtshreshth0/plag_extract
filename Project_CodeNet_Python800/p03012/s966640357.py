N = int(input())
W = input().split()
W = [int(w) for w in W]

S = sum(W)
mini = pow(10, 10)

for i in range(N):
  mi = abs(S - 2 * sum(W[0:i]))
  if mi < mini:
    mini = mi
print(mini)