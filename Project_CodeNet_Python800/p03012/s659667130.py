n = int(input())
w = list(map(int, input().split()))

diff = []

for i in range(n+1):
  diff.append(abs(2*sum(w[:i]) - sum(w)))

print(min(diff))
