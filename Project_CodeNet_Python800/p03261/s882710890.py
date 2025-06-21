N = int(input())
W = [input() for n in range(N)]
a = "Yes"

for n in range(N-1):
  if W[n][-1]!=W[n+1][0] or W.count(W[n])!=1:
    a = "No"

print(a)